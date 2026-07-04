from datetime import datetime, timezone
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, select, update, delete
from shared.settings import settings

engine=create_engine(settings.database_url, pool_pre_ping=True, connect_args={"check_same_thread":False} if settings.database_url.startswith("sqlite") else {})
metadata=MetaData()
query_history=Table("query_history",metadata,Column("id",Integer,primary_key=True,autoincrement=True),Column("ts",String(64),nullable=False),Column("text",Text,nullable=False),Column("intent",String(120),nullable=False),Column("response",Text,nullable=False),Column("feedback",Integer,default=0))

def init(): metadata.create_all(engine)
def add(text,intent,response):
    init()
    with engine.begin() as c:c.execute(query_history.insert().values(ts=datetime.now(timezone.utc).isoformat(),text=text,intent=intent,response=response,feedback=0))
def recent(limit=50):
    init()
    with engine.begin() as c:return [dict(r._mapping) for r in c.execute(select(query_history).order_by(query_history.c.id.desc()).limit(limit))]
def feedback(item_id,score):
    init()
    with engine.begin() as c:c.execute(update(query_history).where(query_history.c.id==item_id).values(feedback=score))
def clear():
    init()
    with engine.begin() as c:c.execute(delete(query_history))

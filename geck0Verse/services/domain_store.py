from shared.storage import sqlite_db
def init(name):
    with sqlite_db(name) as db:db.execute("CREATE TABLE IF NOT EXISTS items (id TEXT PRIMARY KEY,kind TEXT,client TEXT,title TEXT,payload TEXT)")
def list_items(name,kind=None):
    import json;init(name)
    with sqlite_db(name) as db:
        rows=db.execute("SELECT * FROM items"+(" WHERE kind=?" if kind else "")+" ORDER BY title",((kind,) if kind else ())).fetchall();return [{**dict(r),"payload":json.loads(r['payload'])} for r in rows]
def save(name,item):
    import json;init(name)
    with sqlite_db(name) as db:db.execute("INSERT OR REPLACE INTO items VALUES (?,?,?,?,?)",(item['id'],item['kind'],item.get('client','internal'),item['title'],json.dumps(item.get('payload',{}))))

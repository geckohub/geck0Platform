import json, sqlite3
from contextlib import contextmanager
from .settings import settings
@contextmanager
def sqlite_db(name: str):
    path=settings.data_root/name/f"{name}.db"; path.parent.mkdir(parents=True,exist_ok=True); conn=sqlite3.connect(path); conn.row_factory=sqlite3.Row
    try: yield conn; conn.commit()
    finally: conn.close()
def read_json(path,default): return json.loads(path.read_text()) if path.exists() else default
def write_json(path,data):
    path.parent.mkdir(parents=True,exist_ok=True); tmp=path.with_suffix(path.suffix+".tmp"); tmp.write_text(json.dumps(data,indent=2)); tmp.replace(path)

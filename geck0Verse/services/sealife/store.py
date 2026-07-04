from shared.storage import sqlite_db
def init():
    with sqlite_db("sealife") as db:db.execute("CREATE TABLE IF NOT EXISTS listings (id TEXT PRIMARY KEY,town TEXT,bedrooms INTEGER,tenure TEXT,price REAL,payload TEXT,refreshed_at TEXT)")
def replace(items,ts):
    import json;init()
    with sqlite_db("sealife") as db:
        for x in items:db.execute("INSERT OR REPLACE INTO listings VALUES (?,?,?,?,?,?,?)",(x['id'],x['town'],int(x.get('bedrooms',0)),x.get('tenure','unknown'),float(x.get('price',0)),json.dumps(x),ts))
def list_items(towns=None,bedrooms=2):
    import json;init();towns=[t.casefold() for t in (towns or [])]
    with sqlite_db("sealife") as db:items=[json.loads(r['payload']) for r in db.execute("SELECT payload FROM listings WHERE bedrooms>=? ORDER BY price",(bedrooms,)).fetchall()]
    return [x for x in items if not towns or x.get('town','').casefold() in towns]

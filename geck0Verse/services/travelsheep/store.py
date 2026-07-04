from shared.storage import sqlite_db
def init():
    with sqlite_db("travelsheep") as db:db.execute("CREATE TABLE IF NOT EXISTS deals (id TEXT PRIMARY KEY,destination TEXT,lat REAL,lon REAL,depart TEXT,return_date TEXT,travel_price REAL,stay_price REAL,total_price REAL,currency TEXT,source TEXT,summary TEXT,url TEXT,payload TEXT,refreshed_at TEXT)")
def replace(items,refreshed_at):
    import json;init()
    with sqlite_db("travelsheep") as db:
        for d in items:db.execute("INSERT OR REPLACE INTO deals VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(d['id'],d['destination'],d['lat'],d['lon'],d['depart'],d['return'],d['travel_price'],d['stay_price'],d['total_price'],d.get('currency','GBP'),d.get('source','unknown'),d.get('summary',''),d.get('url'),json.dumps(d),refreshed_at))
def list_deals(max_budget=200):
    import json;init()
    with sqlite_db("travelsheep") as db:return [json.loads(r['payload']) for r in db.execute("SELECT payload FROM deals WHERE total_price<=? ORDER BY total_price",(max_budget,)).fetchall()]

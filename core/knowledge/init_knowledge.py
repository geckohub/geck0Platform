import os, sqlite3, pathlib
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
db=root/'knowledge/geck0_knowledge.db'; db.parent.mkdir(parents=True, exist_ok=True)
con=sqlite3.connect(db)
con.executescript('''
CREATE TABLE IF NOT EXISTS nodes(id INTEGER PRIMARY KEY, kind TEXT, name TEXT, data TEXT, updated_at TEXT);
CREATE TABLE IF NOT EXISTS edges(id INTEGER PRIMARY KEY, source INTEGER, target INTEGER, relation TEXT, data TEXT);
CREATE TABLE IF NOT EXISTS observations(id INTEGER PRIMARY KEY, ts TEXT, source TEXT, kind TEXT, lat REAL, lon REAL, data TEXT);
CREATE TABLE IF NOT EXISTS commands(id INTEGER PRIMARY KEY, ts TEXT, persona TEXT, text TEXT, response TEXT);
CREATE TABLE IF NOT EXISTS files(id INTEGER PRIMARY KEY, ts TEXT, project TEXT, path TEXT, kind TEXT, status TEXT);
''')
con.commit(); print(f'Knowledge DB ready: {db}')

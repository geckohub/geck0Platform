import os, sqlite3, pathlib, time
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
db=root/'registry/geck0_registry.db'; db.parent.mkdir(parents=True, exist_ok=True)
con=sqlite3.connect(db)
con.executescript('''
CREATE TABLE IF NOT EXISTS packages(id INTEGER PRIMARY KEY, name TEXT, version TEXT, installed_at TEXT, manifest TEXT);
CREATE TABLE IF NOT EXISTS apps(name TEXT PRIMARY KEY, domain TEXT, status TEXT, command TEXT, description TEXT);
CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, ts TEXT, source TEXT, type TEXT, payload TEXT);
CREATE TABLE IF NOT EXISTS backups(id INTEGER PRIMARY KEY, ts TEXT, path TEXT, status TEXT, note TEXT);
''')
apps=[('crumble','core','ready','crumble','Shared command bus and assistant'),('travelsheep','pinkGeck0','scaffold','travelsheep','Dog-friendly UK weekend deals'),('sealife','pinkGeck0','scaffold','sealife','Shared ownership coastal homes'),('greengeck0','greenGeck0','scaffold','greengeck0','Automated QA/test generation'),('geck0earth','geck0','scaffold','geck0earth','OSM overlays and live map data'),('breadcrumbs','pinkGeck0','scaffold','breadcrumbs','Requirements-to-content factory'),('geck0record','ped0na','scaffold','geck0record','Voice/photo/file/life capture'),('m0nkey','ped0na','scaffold','m0nkey','Daily cockpit'),('li0n','li0n','scaffold','li0n','Events/social/language helper')]
con.executemany('INSERT OR REPLACE INTO apps VALUES (?,?,?,?,?)', apps)
con.commit(); print(f'Registry ready: {db}')

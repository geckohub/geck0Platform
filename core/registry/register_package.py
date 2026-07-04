import sys, json, os, sqlite3, pathlib, datetime
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
db=root/'registry/geck0_registry.db'
manifest=json.load(open(sys.argv[1])) if len(sys.argv)>1 else {'package':'manual','version':'unknown'}
con=sqlite3.connect(db)
con.execute('INSERT INTO packages(name,version,installed_at,manifest) VALUES (?,?,?,?)',(manifest.get('package'),manifest.get('version'),datetime.datetime.utcnow().isoformat(),json.dumps(manifest)))
con.commit(); print('Registered', manifest.get('package'), manifest.get('version'))

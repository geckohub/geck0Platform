import os,sqlite3,pathlib
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
con=sqlite3.connect(root/'registry/geck0_registry.db')
print('🦎 Registered apps')
for r in con.execute('select name,domain,status,description from apps order by domain,name'):
 print(f'{r[0]:14} {r[1]:12} {r[2]:10} {r[3]}')

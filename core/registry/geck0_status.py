import os,sqlite3,pathlib
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
con=sqlite3.connect(root/'registry/geck0_registry.db')
print('🦎 Geck0 Status')
print('Packages:')
for r in con.execute('select name,version,installed_at from packages order by id desc limit 10'):
 print(' ', r)
print('Apps:', con.execute('select count(*) from apps').fetchone()[0])

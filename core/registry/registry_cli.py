#!/usr/bin/env python3
import sqlite3, os, sys, json, socket, datetime
root=os.path.expanduser('~/geck0Platform')
db=os.path.join(root,'registry','ph0enix_registry.db')
os.makedirs(os.path.dirname(db), exist_ok=True)
con=sqlite3.connect(db)
con.execute('create table if not exists devices(id text primary key, name text, kind text, ip text, mac text, role text, last_seen text, notes text)')
con.execute('create table if not exists services(id text primary key, name text, host text, port text, url text, kind text, status text, notes text)')
con.execute('insert or ignore into devices values(?,?,?,?,?,?,?,?)',('je','JelliedEel','raspberry-pi',socket.gethostbyname(socket.gethostname()) if False else '192.168.1.244','','home server',datetime.datetime.now().isoformat(),'main hub'))
con.commit()
cmd=sys.argv[1] if len(sys.argv)>1 else 'summary'
if cmd=='devices':
    for r in con.execute('select id,name,kind,ip,role,last_seen from devices'):
        print(' | '.join(map(str,r)))
elif cmd=='json':
    print(json.dumps({'devices':[dict(zip(['id','name','kind','ip','mac','role','last_seen','notes'],r)) for r in con.execute('select * from devices')]}, indent=2))
else:
    print('Registry ready:', db)

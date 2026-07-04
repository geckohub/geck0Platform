#!/usr/bin/env python3
import os, shutil, sqlite3, json, subprocess
HOME=os.path.expanduser('~')
ROOT=os.path.join(HOME,'geck0Platform')
checks=[]
def ok(name, cond, detail=''):
    checks.append((name, bool(cond), detail))
ok('Root', os.path.isdir(ROOT), ROOT)
ok('Registry DB', os.path.exists(os.path.join(ROOT,'registry','geck0_registry.db')), '')
ok('Knowledge DB', os.path.exists(os.path.join(ROOT,'knowledge','geck0_knowledge.db')), '')
ok('Config env', os.path.exists(os.path.join(ROOT,'config','.env')), 'copy api_keys.example.env if missing')
for c in ['geck0','ph0enix','ped0na','m0nkey','li0n','crumble','breadcrumbs','travelsheep','sealife','greengeck0','geck0earth','geck0record','blackgeck0','cyberx','shopbot']:
    ok('cmd:'+c, shutil.which(c), shutil.which(c) or 'missing')
for d in ['apps/shopbot','dashboards','wiki','updates/incoming','updates/applied','backups']:
    ok('dir:'+d, os.path.isdir(os.path.join(ROOT,d)), '')
print('🔥 Ph0enix / Geck0 Polish Doctor')
for name, good, detail in checks:
    print(('✅' if good else '⚠️'), name, detail)
print('\nSummary:', sum(1 for _,g,_ in checks if g),'/',len(checks),'checks OK')

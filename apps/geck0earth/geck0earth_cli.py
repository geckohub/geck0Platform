import sys, subprocess, pathlib, os
root=pathlib.Path.home()/'geck0Platform/apps/geck0earth/web'
if (sys.argv[1:] or ['serve'])[0]=='serve':
 os.chdir(root); print('🌍 Geck0Earth http://0.0.0.0:8787'); subprocess.run(['python3','-m','http.server','8787'])
else: print('🌍 Geck0Earth commands: serve | layers | import')

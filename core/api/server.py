from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
root=Path(os.environ.get('GECK0_ROOT', Path.home()/'geck0Platform'))
web=root/'apps/geck0earth/web'
if not web.exists(): web=root
os.chdir(web)
print('🦎 Geck0 PWA serving on http://0.0.0.0:8787')
ThreadingHTTPServer(('0.0.0.0',8787), SimpleHTTPRequestHandler).serve_forever()

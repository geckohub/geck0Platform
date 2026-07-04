import os, json, urllib.request, urllib.parse
from pathlib import Path
from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path.home() / "geck0Platform"
WEB = ROOT / "web" / "fusebox"
ENV = ROOT / "config" / ".env"

app = FastAPI(title="Fusebox Web", version="5.1")

if (WEB / "static").exists():
    app.mount("/static", StaticFiles(directory=str(WEB / "static")), name="static")

def env_get(key: str, default: str = "") -> str:
    if not ENV.exists(): return default
    for line in ENV.read_text(errors="ignore").splitlines():
        if line.strip().startswith(key + "="):
            return line.split("=",1)[1].strip().strip('"').strip("'")
    return default

@app.get("/", response_class=HTMLResponse)
def home():
    return (WEB / "index.html").read_text(errors="ignore")

@app.get("/earth", response_class=HTMLResponse)
def earth():
    return (WEB / "earth.html").read_text(errors="ignore")

@app.get("/api/status")
def status():
    return {"status":"ok","service":"fusebox-web","version":"5.1","root":str(ROOT)}

@app.get("/api/tfl/lines")
def tfl_lines():
    key = env_get("TFL_APP_KEY")
    if not key:
        return {"error":"TFL_APP_KEY missing in ~/geck0Platform/config/.env"}
    url = "https://api.tfl.gov.uk/Line/Mode/tube,overground,dlr,tram,elizabeth-line/Status?" + urllib.parse.urlencode({"app_key":key})
    try:
        with urllib.request.urlopen(url, timeout=10) as r:
            return json.loads(r.read().decode())
    except Exception as e:
        return {"error":str(e)}

@app.get("/api/layer/{name}")
def layer(name: str):
    candidates = [
        ROOT / "geck0Earth" / "layers" / f"{name}.geojson",
        ROOT / "geck0Earth" / "layers" / f"{name}_latest.geojson",
        ROOT / "apps" / "travelsheep" / "data" / "osm_overlay.geojson" if name == "travelsheep" else None,
    ]
    for p in candidates:
        if p and p.exists():
            return FileResponse(str(p), media_type="application/geo+json")
    return JSONResponse({"type":"FeatureCollection","features":[],"note":f"No layer data for {name} yet"})

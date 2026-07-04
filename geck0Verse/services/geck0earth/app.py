from datetime import datetime,timezone
from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.audit import audit
from shared.models import Health
from shared.registry import load_yaml
from shared.storage import sqlite_db
from .connectors import weather,air_quality,marine,earthquakes,geocode
from shared.web import configure_web
app=FastAPI(title="Geck0Earth",version="2.0.0")
configure_web(app)
class Observation(BaseModel):source:str;layer:str;lat:float;lon:float;payload:dict=Field(default_factory=dict)
def init():
    with sqlite_db("geck0earth") as db:db.execute("CREATE TABLE IF NOT EXISTS observations (id INTEGER PRIMARY KEY,ts TEXT,source TEXT,layer TEXT,lat REAL,lon REAL,payload TEXT)")
@app.get("/health",response_model=Health)
def health():return Health(service="geck0earth")
@app.get("/v1/layers")
def layers(_:str=Depends(require_token)):return load_yaml("layers.yaml")
@app.get("/v1/realtime")
async def realtime(lat:float=51.5074,lon:float=-0.1278,layers:str="weather,air_quality",_:str=Depends(require_token)):
    selected={x.strip() for x in layers.split(',')};out={}
    if 'weather' in selected:out['weather']=await weather(lat,lon)
    if 'air_quality' in selected:out['air_quality']=await air_quality(lat,lon)
    if 'marine' in selected:out['marine']=await marine(lat,lon)
    if 'earthquakes' in selected:out['earthquakes']=await earthquakes()
    return {"lat":lat,"lon":lon,"layers":out,"generated_at":datetime.now(timezone.utc).isoformat()}
@app.post("/v1/observations")
def ingest(obs:Observation,_:str=Depends(require_token)):
    import json;init()
    with sqlite_db("geck0earth") as db:db.execute("INSERT INTO observations(ts,source,layer,lat,lon,payload) VALUES (?,?,?,?,?,?)",(datetime.now(timezone.utc).isoformat(),obs.source,obs.layer,obs.lat,obs.lon,json.dumps(obs.payload)))
    audit("geck0earth","observation",{"source":obs.source,"layer":obs.layer});return {"accepted":True}
@app.get("/v1/metrics")
def metrics(_:str=Depends(require_token)):
    init()
    with sqlite_db("geck0earth") as db:count=db.execute("SELECT count(*) c FROM observations").fetchone()['c']
    return {"observations":count,"layer_count":len(load_yaml('layers.yaml').get('layers',[])),"mode":"public-data-and-local-ingestion"}

@app.get("/v1/geocode")
async def geocode_location(query:str,_:str=Depends(require_token)):return await geocode(query)

from datetime import datetime,timezone
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends,Query
from shared.auth import require_token
from shared.audit import audit
from shared.models import Health
from .connectors import load_all
from .store import replace,list_items
from shared.web import configure_web
@asynccontextmanager
async def lifespan(app: FastAPI):
    if not list_items([],0): await refresh("startup")
    yield
app=FastAPI(title="SeaLife",version="2.0.0",lifespan=lifespan)
configure_web(app)
@app.get("/health",response_model=Health)
def health():return Health(service="sealife")
async def refresh(actor="api"):
    items=await load_all();replace(items,datetime.now(timezone.utc).isoformat());audit("sealife","refresh",{"count":len(items),"actor":actor});return {"refreshed":len(items)}
@app.post("/v1/refresh")
async def refresh_endpoint(_:str=Depends(require_token)):return await refresh()
@app.get("/v1/listings")
def listings(town:list[str]=Query(default=[]),bedrooms:int=2,_:str=Depends(require_token)):return {"listings":list_items(town,bedrooms)}
@app.get("/v1/map")
def map_data(town:list[str]=Query(default=[]),_:str=Depends(require_token)):
    items=list_items(town,2);return {"points":[{"id":x['id'],"lat":float(x['lat']),"lon":float(x['lon']),"title":x['title'],"category":"property","properties":x} for x in items]}

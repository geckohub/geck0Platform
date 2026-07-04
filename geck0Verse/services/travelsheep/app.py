from datetime import datetime,timezone
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI,Depends,HTTPException
from shared.auth import require_token
from shared.audit import audit
from shared.models import Health
from .connectors import sample_deals,enrich_weather,generic_json_feed,ticketmaster_events
from .store import replace,list_deals
from .amadeus import flight_offers
import os
from shared.web import configure_web
@asynccontextmanager
async def lifespan(app: FastAPI):
    if not list_deals(10000):
        initial=await sample_deals();replace(initial,datetime.now(timezone.utc).isoformat())
    yield
app=FastAPI(title="TravelSheep",version="2.0.0",lifespan=lifespan)
configure_web(app)
@app.get("/health",response_model=Health)
def health():return Health(service="travelsheep")
async def refresh(actor="api"):
    items=await sample_deals();items.extend(await generic_json_feed());items=await enrich_weather(items)
    events=await asyncio.gather(*(ticketmaster_events(d["destination"]) for d in items[:8]))
    for d,event_list in zip(items[:8],events):d["events"]=event_list
    replace(items,datetime.now(timezone.utc).isoformat());audit("travelsheep","refresh",{"count":len(items),"actor":actor});return {"refreshed":len(items)}
@app.post("/v1/refresh")
async def refresh_endpoint(_:str=Depends(require_token)):return await refresh()
@app.get("/v1/deals")
def deals(max_budget:float=200,_:str=Depends(require_token)):return {"deals":list_deals(max_budget),"max_budget":max_budget}
@app.get("/v1/map")
def map_data(max_budget:float=200,_:str=Depends(require_token)):return {"points":[{"id":d['id'],"lat":d['lat'],"lon":d['lon'],"title":d['destination'],"category":"travel","properties":d} for d in list_deals(max_budget)]}

@app.get("/v1/connectors/status")
def connector_status(_:str=Depends(require_token)):
    return {"open_meteo":True,"ticketmaster":bool(os.getenv("TICKETMASTER_API_KEY")),"amadeus":bool(os.getenv("AMADEUS_CLIENT_ID") and os.getenv("AMADEUS_CLIENT_SECRET")),"json_feed":bool(os.getenv("TRAVELSHEEP_JSON_FEED_URL"))}
@app.get("/v1/connectors/amadeus/flights")
async def amadeus_flights(origin:str,destination:str,departure_date:str,return_date:str|None=None,max_price:float=200,_:str=Depends(require_token)):
    try:return await flight_offers(origin,destination,departure_date,return_date,max_price=max_price)
    except Exception as exc:raise HTTPException(400,str(exc))

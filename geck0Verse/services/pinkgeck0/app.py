from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.models import Health
from services.domain_store import list_items,save
from shared.web import configure_web
app=FastAPI(title="Pink Geck0",version="2.0.0")
configure_web(app)
SEED=[{'id': 'travelsheep', 'kind': 'project', 'title': 'TravelSheep', 'client': 'internal', 'payload': {'schedule': 'Thursday 02:00 Europe/London'}}, {'id': 'sealife', 'kind': 'project', 'title': 'SeaLife', 'client': 'internal', 'payload': {'schedule': 'Daily 11:00 Europe/London'}}, {'id': 'breadcrumbs', 'kind': 'project', 'title': 'BreadCrumbs', 'client': 'internal', 'payload': {'repo_automation': True}}]
ALLOWED=['project', 'client-site', 'automation', 'experiment']

def ensure_seed():
    existing=list_items("pinkgeck0")
    if not existing:
        for item in SEED: save("pinkgeck0",item)

class Item(BaseModel):id:str;kind:str;title:str;client:str="internal";payload:dict=Field(default_factory=dict)
@app.get("/health",response_model=Health)
def health():return Health(service="pinkgeck0")
@app.get("/v1/items")
def items(kind:str|None=None,_:str=Depends(require_token)):
    ensure_seed();return {"items":list_items("pinkgeck0",kind)}
@app.post("/v1/items")
def add(item:Item,_:str=Depends(require_token)):
    if item.kind not in ALLOWED:return {"ok":False,"error":"Unsupported kind","allowed":ALLOWED}
    save("pinkgeck0",item.model_dump());return {"ok":True,"id":item.id}
@app.get("/v1/capabilities")
def capabilities(_:str=Depends(require_token)):return {"kinds":ALLOWED}

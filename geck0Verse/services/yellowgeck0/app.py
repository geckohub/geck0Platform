from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.models import Health
from services.domain_store import list_items,save
from shared.web import configure_web
app=FastAPI(title="Yellow Geck0",version="2.0.0")
configure_web(app)
SEED=[{'id': 'robot-rainforest', 'kind': 'shop', 'title': 'Robot Rainforest', 'client': 'internal', 'payload': {'status': 'drop-in-ready', 'category': 'speciality ecommerce'}}, {'id': 'demo-product', 'kind': 'product', 'title': 'Sample speciality product', 'client': 'robot-rainforest', 'payload': {'price': 12.5, 'currency': 'GBP'}}]
ALLOWED=['shop', 'product', 'order', 'client-site']

def ensure_seed():
    existing=list_items("yellowgeck0")
    if not existing:
        for item in SEED: save("yellowgeck0",item)

class Item(BaseModel):id:str;kind:str;title:str;client:str="internal";payload:dict=Field(default_factory=dict)
@app.get("/health",response_model=Health)
def health():return Health(service="yellowgeck0")
@app.get("/v1/items")
def items(kind:str|None=None,_:str=Depends(require_token)):
    ensure_seed();return {"items":list_items("yellowgeck0",kind)}
@app.post("/v1/items")
def add(item:Item,_:str=Depends(require_token)):
    if item.kind not in ALLOWED:return {"ok":False,"error":"Unsupported kind","allowed":ALLOWED}
    save("yellowgeck0",item.model_dump());return {"ok":True,"id":item.id}
@app.get("/v1/capabilities")
def capabilities(_:str=Depends(require_token)):return {"kinds":ALLOWED}

from fastapi import FastAPI,Depends
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.models import Health
from services.domain_store import list_items,save
from shared.web import configure_web
app=FastAPI(title="Blue Geck0",version="2.0.0")
configure_web(app)
SEED=[{'id': 'blue-gallery-demo', 'kind': 'gallery', 'title': 'Blue Geck0 Gallery', 'client': 'internal', 'payload': {'description': 'Responsive gallery and design-business storefront foundation'}}, {'id': 'blue-print-demo', 'kind': 'print-product', 'title': 'Geck0 Art Print', 'client': 'internal', 'payload': {'materials': ['paper', 'canvas', 'metal'], 'status': 'sample'}}]
ALLOWED=['asset', 'gallery', 'print-product', 'client']

def ensure_seed():
    existing=list_items("bluegeck0")
    if not existing:
        for item in SEED: save("bluegeck0",item)

class Item(BaseModel):id:str;kind:str;title:str;client:str="internal";payload:dict=Field(default_factory=dict)
@app.get("/health",response_model=Health)
def health():return Health(service="bluegeck0")
@app.get("/v1/items")
def items(kind:str|None=None,_:str=Depends(require_token)):
    ensure_seed();return {"items":list_items("bluegeck0",kind)}
@app.post("/v1/items")
def add(item:Item,_:str=Depends(require_token)):
    if item.kind not in ALLOWED:return {"ok":False,"error":"Unsupported kind","allowed":ALLOWED}
    save("bluegeck0",item.model_dump());return {"ok":True,"id":item.id}
@app.get("/v1/capabilities")
def capabilities(_:str=Depends(require_token)):return {"kinds":ALLOWED}

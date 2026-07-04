from pathlib import Path
import os
from uuid import uuid4
import os
from fastapi import FastAPI,Depends,UploadFile,File,HTTPException
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.audit import audit
from shared.intents import classify,suggestions as make_suggestions
from shared.models import Health
from shared.registry import projects
from shared.settings import settings
from .dispatcher import execute
from .history import add,recent,feedback,clear
from .llm import ask_llm
from shared.web import configure_web
app=FastAPI(title="Crumble / Geck0 Hub",version="2.0.0")
configure_web(app)
class ChatRequest(BaseModel): message:str=Field(min_length=1,max_length=8000)
class FeedbackRequest(BaseModel): score:int=Field(ge=-1,le=1)
@app.get("/health",response_model=Health)
def health():return Health(service="hub")
@app.get("/v1/domains")
def domains(_:str=Depends(require_token)):
    public=os.getenv("PUBLIC_BASE_URL","http://localhost:8088").rstrip("/")
    items=[]
    for item in projects():
        copy=dict(item)
        if copy.get("dashboard"):
            copy["dashboard"]=copy["dashboard"].replace("http://localhost:8088",public)
        items.append(copy)
    return {"domains":items}
@app.post("/v1/chat")
async def chat(req:ChatRequest,_:str=Depends(require_token)):
    intent=classify(req.message); data=None
    if intent.get("action"):
        try:data=await execute(intent["action"])
        except Exception as exc:data={"error":str(exc)}
    llm=await ask_llm(req.message,"" if data is None else str(data)[:5000])
    answer=llm or (f"I matched {intent['name']} and retrieved the latest domain data." if data is not None else "I can control TravelSheep, SeaLife, Geck0Earth, projects and uploads. Try asking for the latest deals, listings or layers.")
    add(req.message,intent["name"],answer); audit("hub","chat",{"intent":intent["name"]}); return {"answer":answer,"intent":intent,"data":data}
@app.get("/v1/history")
def history(limit:int=50,_:str=Depends(require_token)):return {"items":recent(max(1,min(limit,200)))}
@app.post("/v1/history/{item_id}/feedback")
def history_feedback(item_id:int,req:FeedbackRequest,_:str=Depends(require_token)):feedback(item_id,req.score);return {"ok":True}
@app.get("/v1/suggestions")
def suggestions(_:str=Depends(require_token)):return {"suggestions":make_suggestions([r["text"] for r in recent(100)])}
@app.delete("/v1/history")
def clear_history(_:str=Depends(require_token)):
    clear(); audit("hub","history_clear",{}); return {"cleared":True}

@app.post("/v1/uploads")
async def upload(file:UploadFile=File(...),_:str=Depends(require_token)):
    limit=int(os.getenv("GECK0_UPLOAD_LIMIT_MB","25"))*1024*1024; data=await file.read(limit+1)
    if len(data)>limit:raise HTTPException(413,"Upload too large")
    safe=Path(file.filename or "upload.bin").name; target=settings.data_root/"hub"/"uploads"/f"{uuid4().hex}_{safe}"; target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data);audit("hub","upload",{"filename":safe,"bytes":len(data)});return {"id":target.name,"filename":safe,"bytes":len(data)}

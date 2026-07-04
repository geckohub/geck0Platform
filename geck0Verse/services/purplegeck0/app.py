from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel
from cryptography.fernet import Fernet
import os
from shared.auth import require_token
from shared.storage import sqlite_db
from shared.models import Health
from shared.web import configure_web
app=FastAPI(title="Purple Geck0",version="2.0.0")
configure_web(app)
def cipher():
    try:return Fernet(os.getenv("GECK0_FERNET_KEY","").encode())
    except Exception:raise HTTPException(503,"GECK0_FERNET_KEY is invalid")
def init():
    with sqlite_db("purplegeck0") as db:db.execute("CREATE TABLE IF NOT EXISTS secrets (name TEXT PRIMARY KEY,value BLOB,category TEXT,notes TEXT)");db.execute("CREATE TABLE IF NOT EXISTS webhooks (name TEXT PRIMARY KEY,url BLOB,platform TEXT,enabled INTEGER)")
class Secret(BaseModel):name:str;value:str;category:str="api-key";notes:str=""
class Webhook(BaseModel):name:str;url:str;platform:str;enabled:bool=True
@app.get("/health",response_model=Health)
def health():return Health(service="purplegeck0")
@app.post("/v1/secrets")
def save_secret(s:Secret,_:str=Depends(require_token)):
    init();enc=cipher().encrypt(s.value.encode())
    with sqlite_db("purplegeck0") as db:db.execute("INSERT OR REPLACE INTO secrets VALUES (?,?,?,?)",(s.name,enc,s.category,s.notes))
    return {"saved":s.name}
@app.get("/v1/secrets")
def list_secrets(_:str=Depends(require_token)):
    init()
    with sqlite_db("purplegeck0") as db:return {"secrets":[dict(r) for r in db.execute("SELECT name,category,notes FROM secrets ORDER BY name").fetchall()]}
@app.post("/v1/webhooks")
def save_webhook(w:Webhook,_:str=Depends(require_token)):
    init();enc=cipher().encrypt(w.url.encode())
    with sqlite_db("purplegeck0") as db:db.execute("INSERT OR REPLACE INTO webhooks VALUES (?,?,?,?)",(w.name,enc,w.platform,int(w.enabled)))
    return {"saved":w.name}

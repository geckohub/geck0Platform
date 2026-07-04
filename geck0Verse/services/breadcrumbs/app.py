from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.audit import audit
from shared.models import Health
from .repos import init_repo,commit,ROOT
from shared.web import configure_web
app=FastAPI(title="BreadCrumbs",version="2.0.0")
configure_web(app)
class InitRequest(BaseModel):name:str=Field(min_length=2,max_length=80);template:str="static-site"
class CommitRequest(BaseModel):message:str=Field(min_length=2,max_length=200)
@app.get("/health",response_model=Health)
def health():return Health(service="breadcrumbs")
@app.get("/v1/projects")
def projects(_:str=Depends(require_token)):ROOT.mkdir(parents=True,exist_ok=True);return {"projects":[p.name for p in ROOT.iterdir() if p.is_dir()]}
@app.post("/v1/projects")
def create(req:InitRequest,_:str=Depends(require_token)):
    try:p=init_repo(req.name,req.template)
    except Exception as exc:raise HTTPException(400,str(exc))
    audit("breadcrumbs","init",{"project":p.name});return {"project":p.name,"path":str(p)}
@app.post("/v1/projects/{name}/commit")
def commit_project(name:str,req:CommitRequest,_:str=Depends(require_token)):
    try:r=commit(name,req.message)
    except Exception as exc:raise HTTPException(400,str(exc))
    audit("breadcrumbs","commit",{"project":name,"returncode":r['returncode']});return r

from fastapi import FastAPI,Depends,HTTPException
from pydantic import BaseModel,Field
from shared.auth import require_token
from shared.audit import audit
from shared.models import Health
from .runner import run_checks,SAFE_TESTS
from .reports import write_report
from .delivery import deliver
from shared.web import configure_web
app=FastAPI(title="Green Geck0",version="2.0.0")
configure_web(app)
class TestJob(BaseModel):url:str;languages:list[str]=Field(default_factory=list);tests:list[str]=Field(default_factory=lambda:["http","headers","tls"]);evidence:list[str]=Field(default_factory=lambda:["text"]);outputs:list[str]=Field(default_factory=lambda:["json","html"]);delivery:dict=Field(default_factory=dict);tier:str="internal"
@app.get("/health",response_model=Health)
def health():return Health(service="greengeck0")
@app.get("/v1/capabilities")
def caps(_:str=Depends(require_token)):return {"safe_tests":sorted(SAFE_TESTS),"evidence":["text","screenshot-planned","video-planned"],"outputs":["json","html","pdf","sqlite-planned"],"delivery":["webhook","email","git"]}
@app.post("/v1/tests")
async def test(job:TestJob,_:str=Depends(require_token)):
    try:result=await run_checks(job.url,job.tests)
    except Exception as exc:raise HTTPException(400,str(exc))
    result["request"]=job.model_dump();rid,outputs=write_report(result,job.outputs);delivery_status=await deliver(result,outputs,job.delivery);audit("greengeck0","test",{"id":rid,"url":job.url});return {"id":rid,"result":result,"outputs":outputs,"delivery":delivery_status}

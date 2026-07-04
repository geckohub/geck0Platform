import asyncio
from contextlib import asynccontextmanager
from datetime import datetime
from zoneinfo import ZoneInfo
from fastapi import FastAPI,Depends,HTTPException
from shared.auth import require_token
from shared.http import post_json
from shared.registry import load_yaml
from shared.storage import read_json,write_json
from shared.settings import settings
from shared.web import configure_web
STATE=settings.data_root/"scheduler"/"state.json";TASK=None
def due(job,now,last):
    weekday=job.get("weekday","*")
    if weekday!="*" and int(weekday)!=now.weekday():return False
    if now.hour!=int(job.get("hour",0)) or now.minute!=int(job.get("minute",0)):return False
    return last.get(job['id'])!=now.strftime("%Y-%m-%d-%H-%M")
async def run_job(job):return await post_json(job['url'],{},headers={"X-Geck0-Token":settings.internal_token})
async def loop():
    tz=ZoneInfo(load_yaml('schedules.yaml').get('timezone','Europe/London'))
    while True:
        now=datetime.now(tz);state=read_json(STATE,{})
        for job in load_yaml('schedules.yaml').get('jobs',[]):
            if due(job,now,state):
                try:state[job['id']]=now.strftime("%Y-%m-%d-%H-%M");state[job['id']+'_result']=await run_job(job)
                except Exception as exc:state[job['id']+'_error']=str(exc)
                write_json(STATE,state)
        await asyncio.sleep(30)
@asynccontextmanager
async def lifespan(app: FastAPI):
    global TASK
    TASK=asyncio.create_task(loop())
    try:
        yield
    finally:
        if TASK:
            TASK.cancel()
            try:
                await TASK
            except asyncio.CancelledError:
                pass
app=FastAPI(title="Geck0 Scheduler",version="2.0.0",lifespan=lifespan)
configure_web(app)
@app.get("/health")
def health():return {"service":"scheduler","status":"ok"}
@app.get("/v1/jobs")
def jobs(_:str=Depends(require_token)):return {"jobs":load_yaml('schedules.yaml').get('jobs',[]),"state":read_json(STATE,{})}
@app.post("/v1/jobs/{job_id}/run")
async def manual(job_id:str,_:str=Depends(require_token)):
    job=next((j for j in load_yaml('schedules.yaml').get('jobs',[]) if j['id']==job_id),None)
    if not job:raise HTTPException(404,"Unknown job")
    return await run_job(job)

from shared.http import fetch_json,post_json
from shared.registry import projects
async def execute(action):
    if not action:return None
    if action=="LOCAL projects":return {"projects":projects()}
    method,url=action.split(" ",1); return await (fetch_json(url) if method=="GET" else post_json(url,{}))

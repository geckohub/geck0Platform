import httpx
async def fetch_json(url: str, *, params: dict | None=None, headers: dict | None=None, timeout: float=12.0):
    async with httpx.AsyncClient(timeout=timeout,follow_redirects=True) as client:
        r=await client.get(url,params=params,headers=headers); r.raise_for_status(); return r.json()
async def post_json(url: str, payload: dict | None=None, headers: dict | None=None, timeout: float=30.0):
    async with httpx.AsyncClient(timeout=timeout,follow_redirects=True) as client:
        r=await client.post(url,json=payload or {},headers=headers); r.raise_for_status(); return r.json()

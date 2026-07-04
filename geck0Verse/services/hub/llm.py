import os,httpx
async def ask_llm(message:str,context:str=""):
    if os.getenv("CRUMBLE_LLM_PROVIDER","none").lower()!="ollama": return None
    base=os.getenv("OLLAMA_BASE_URL","http://host.docker.internal:11434").rstrip("/"); model=os.getenv("OLLAMA_MODEL","qwen3:4b")
    prompt="You are Crumble, the helpful Geck0verse control assistant. Be concise and honest.\n"+(f"Context:\n{context}\n" if context else "")+f"User: {message}"
    try:
        async with httpx.AsyncClient(timeout=45) as client:
            r=await client.post(f"{base}/api/chat",json={"model":model,"stream":False,"messages":[{"role":"user","content":prompt}]}); r.raise_for_status(); return r.json().get("message",{}).get("content")
    except Exception: return None

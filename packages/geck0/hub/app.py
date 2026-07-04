from fastapi import FastAPI
from datetime import datetime

app = FastAPI(title="Geck0Hub", version="0.1")

@app.get("/")
def home():
    return {
        "service": "Geck0Hub",
        "status": "online",
        "time": datetime.now().isoformat(),
        "sections": ["Dashboard", "Geck0Docs", "Plugins", "Updates", "Search", "Crumble", "CyberX"]
    }

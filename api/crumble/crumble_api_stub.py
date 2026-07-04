#!/usr/bin/env python3
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Geck0 Crumble API", version="0.2")

class Command(BaseModel):
    text: str

@app.get("/status")
def status():
    return {
        "service": "crumble-api",
        "status": "online",
        "version": "0.2",
        "time": datetime.now().isoformat()
    }

@app.get("/search")
def search(q: str):
    return {
        "query": q,
        "status": "placeholder",
        "route": "Crumble -> CyberX -> Geck0 Search -> Knowledge Graph"
    }

@app.post("/command")
def command(cmd: Command):
    return {
        "received": cmd.text,
        "status": "accepted",
        "future_route": "Crumble command router"
    }

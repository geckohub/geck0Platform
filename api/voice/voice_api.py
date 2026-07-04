#!/usr/bin/env python3
from fastapi import FastAPI
from datetime import datetime
import subprocess

app = FastAPI(title="Geck0 Voice API", version="0.1")

def cmd(command):
    try:
        return subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=3).strip()
    except Exception:
        return "n/a"

@app.get("/status")
def status():
    return {
        "service": "geck0-voice-api",
        "status": "online",
        "wake_word": "Crumble",
        "engine": "openWakeWord planned",
        "mode": "diagnostic",
        "time": datetime.now().isoformat()
    }

@app.get("/diagnostics")
def diagnostics():
    return {
        "voice_status": cmd("cd ~/geck0Platform && source .venv/bin/activate && python services/voice/voice_status.py")
    }

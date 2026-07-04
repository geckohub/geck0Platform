#!/usr/bin/env python3
import json
import subprocess
from datetime import datetime

def check_import(name):
    try:
        __import__(name)
        return True
    except Exception:
        return False

def cmd(command):
    try:
        return subprocess.check_output(command, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=3).strip()
    except Exception:
        return "n/a"

status = {
    "service": "geck0-voice",
    "wake_word": "Crumble",
    "engine": "openWakeWord",
    "mode": "diagnostic",
    "always_listening": False,
    "time": datetime.now().isoformat(),
    "python_modules": {
        "openwakeword": check_import("openwakeword"),
        "sounddevice": check_import("sounddevice"),
        "numpy": check_import("numpy"),
        "requests": check_import("requests")
    },
    "audio_devices": cmd("python3 -m sounddevice 2>/dev/null || true"),
    "crumble_api": cmd("curl -s http://localhost:8890/status || true")
}

print(json.dumps(status, indent=2))

#!/usr/bin/env python3
"""
Geck0 Voice Pack 1 - Crumble wake listener placeholder.

Current role:
- Confirms voice stack path exists.
- Provides safe diagnostic service.
- Does NOT start always-listening audio yet.

Next role:
- OpenWakeWord listens for "Crumble"
- Sends activation event to Crumble API
- STT/VAD/TTS added in Voice Pack 2
"""

import time
from datetime import datetime
from pathlib import Path

LOG = Path.home() / "geck0Platform" / "updates" / "logs" / "voiceWakeListener.log"

def log(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")

log("Geck0 Voice listener placeholder started. Wake word target: Crumble.")

while True:
    time.sleep(30)
    log("Voice placeholder alive. Always-listening wake detection not enabled yet.")

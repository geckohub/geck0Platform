from pathlib import Path
from datetime import datetime
import os

GECK0_HOME = Path(os.environ.get("GECK0_HOME", Path.home() / "geck0Platform"))

def log(channel: str, message: str):
    log_dir = GECK0_HOME / "logs" / channel
    log_dir.mkdir(parents=True, exist_ok=True)
    line = f"[{datetime.now().isoformat()}] {message}\n"
    with (log_dir / f"{channel}.log").open("a") as f:
        f.write(line)
    return line

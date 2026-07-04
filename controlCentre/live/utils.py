import subprocess
from pathlib import Path

GECK0_HOME = Path.home() / "geck0Platform"
TG_HOST = "lucy@192.168.1.172"
SSH_PORT = "1991"

def sh(cmd: str, timeout: int = 4) -> str:
    try:
        return subprocess.check_output(
            cmd, shell=True, text=True, stderr=subprocess.DEVNULL, timeout=timeout
        ).strip()
    except Exception:
        return "n/a"

def tg(cmd: str, timeout: int = 6) -> str:
    safe = cmd.replace('"', '\\"')
    return sh(f'ssh -p {SSH_PORT} -o BatchMode=yes -o ConnectTimeout=2 {TG_HOST} "{safe}"', timeout)

def service_status(name: str) -> str:
    return "● ONLINE" if sh(f"systemctl is-active {name}") == "active" else "○ OFFLINE"

def bar(percent, width=16) -> str:
    try:
        p = float(percent)
    except Exception:
        p = 0
    filled = int((p / 100) * width)
    return "█" * filled + "░" * (width - filled)

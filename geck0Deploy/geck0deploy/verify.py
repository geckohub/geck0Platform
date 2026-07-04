from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from .utils import root


def exists(path: Path, executable: bool = False) -> str:
    if executable:
        return "OK" if path.exists() and path.stat().st_mode & 0o111 else "MISSING/not executable"
    return "OK" if path.exists() else "MISSING"


def verify() -> None:
    r = root()
    print("Geck0Deploy Python Verify")
    print("=========================")
    print(f"Root: {r}")
    print("\n[Git]")
    subprocess.run(["git", "-C", str(r), "status", "--short"], check=False)
    subprocess.run(["git", "-C", str(r), "remote", "-v"], check=False)
    print("\n[Folders]")
    for d in ["governance", "governance/tg", "governance/tg/pending_updates", "geck0Deploy", "geck0Deploy/docs"]:
        print(f"{exists(r/d)}: {d}")
    print("\n[Executables]")
    for f in ["geck0Deploy/bin/geck0", "geck0Deploy/bin/geck0-py"]:
        print(f"{exists(r/f, True)}: {f}")
    print("\n[Disk]")
    subprocess.run(["df", "-h", "/"], check=False)
    print("\n[Linode SSH]")
    rc = subprocess.run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=8", "pinkgeck0@172.233.15.159", "echo OK"], check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    print("OK: Linode SSH works" if rc == 0 else "WARN: Linode SSH not passwordless yet")
    print("\n[TG Queue]")
    q = r / "governance" / "tg" / "pending_updates"
    if q.exists():
        for p in sorted(q.glob("*.tar.gz"))[-10:]:
            print(p.name)

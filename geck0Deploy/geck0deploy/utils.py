from __future__ import annotations

import os
import subprocess
from pathlib import Path
from datetime import datetime


def root() -> Path:
    return Path(os.environ.get("GECK0_ROOT", Path.home() / "geck0Platform")).expanduser()


def now_stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def run(cmd: list[str], cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess:
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=str(cwd) if cwd else None, text=True, check=check)


def read_text(path: Path, default: str = "") -> str:
    try:
        return path.read_text()
    except FileNotFoundError:
        return default

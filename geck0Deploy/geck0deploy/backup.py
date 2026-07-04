from __future__ import annotations

import tarfile
from pathlib import Path
from .utils import root, ensure_dir, now_stamp, run

EXCLUDES = {
    ".git", "__pycache__", "node_modules", ".venv", "venv", "reports",
    "updates", "storage", "logs", "clients", "client", "evidence", "screenshots"
}
SUFFIX_EXCLUDES = (".pyc", ".tar.gz", ".zip", ".mp4", ".mov", ".mkv", ".iso")


def _skip(path: Path) -> bool:
    parts = set(path.parts)
    if parts & EXCLUDES:
        return True
    return path.name.endswith(SUFFIX_EXCLUDES)


def architecture_backup() -> Path:
    r = root()
    out_dir = Path.home() / "geck0_architecture_backups"
    ensure_dir(out_dir)
    out = out_dir / f"geck0verse_architecture_{now_stamp()}.tar.gz"
    with tarfile.open(out, "w:gz") as tf:
        for p in r.rglob("*"):
            rel = p.relative_to(r.parent)
            if _skip(p.relative_to(r)):
                continue
            tf.add(p, arcname=str(rel), recursive=False)
    print(f"Created architecture backup: {out}")
    return out


def backup_linode() -> None:
    out = architecture_backup()
    user = "pinkgeck0"
    host = "172.233.15.159"
    dest = "/home/pinkgeck0/backups/software_architecture"
    run(["ssh", f"{user}@{host}", f"mkdir -p {dest}"])
    run(["scp", str(out), f"{user}@{host}:{dest}/"])
    print("Uploaded to Linode")

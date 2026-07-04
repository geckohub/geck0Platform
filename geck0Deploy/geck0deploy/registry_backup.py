from pathlib import Path
import tarfile
import datetime

from .projects import parse_projects_yaml
from .utils import root

EXCLUDES = {
    ".git", "__pycache__", ".venv", "venv", "node_modules",
    "logs", "reports", "storage", "updates", "backups",
    "clients", "evidence", "screenshots"
}

BAD_SUFFIXES = {
    ".pyc", ".tar.gz", ".zip", ".mp4", ".mov", ".mkv", ".iso"
}

def should_skip(path: Path):
    if path.name in EXCLUDES:
        return True
    return any(str(path).endswith(s) for s in BAD_SUFFIXES)

def add_project(tar, project_name, project_path):
    base = Path(project_path).expanduser()
    if not base.exists():
        print(f"SKIP missing: {project_name} -> {base}")
        return

    for item in base.rglob("*"):
        if any(should_skip(part) for part in item.parents) or should_skip(item):
            continue
        arcname = Path(project_name) / item.relative_to(base)
        tar.add(item, arcname=arcname, recursive=False)

def main(args):
    registry = root() / "governance" / "projects" / "projects.yaml"
    if not registry.exists():
        print(f"Missing registry: {registry}")
        return

    projects = parse_projects_yaml(registry)
    out_dir = Path.home() / "geck0_architecture_backups"
    out_dir.mkdir(parents=True, exist_ok=True)

    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = out_dir / f"geck0verse_registry_architecture_{stamp}.tar.gz"

    with tarfile.open(out, "w:gz") as tar:
        for name, meta in projects.items():
            if meta.get("backup", "true").lower() == "false":
                continue
            add_project(tar, name, meta.get("path", ""))

    print(f"Created registry architecture backup: {out}")

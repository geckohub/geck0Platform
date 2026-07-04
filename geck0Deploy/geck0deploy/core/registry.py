from pathlib import Path
from .config import root


def registry_path() -> Path:
    return root() / "governance" / "projects" / "projects.yaml"


def parse_simple_yaml(path: Path) -> dict:
    projects = {}
    current = None
    if not path.exists():
        return projects
    for line in path.read_text().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if line.startswith("  ") and line.strip().endswith(":"):
            current = line.strip().rstrip(":")
            projects[current] = {}
        elif current and line.startswith("    ") and ":" in line:
            k, v = line.strip().split(":", 1)
            projects[current][k.strip()] = v.strip().strip('"')
    return projects


def load_projects() -> dict:
    return parse_simple_yaml(registry_path())


def ensure_default_registry():
    p = registry_path()
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text(f'''projects:\n  geck0Platform:\n    path: {root()}\n    family: geck0\n    status: active\n    host: JE\n    backup: true\n''')
    return p

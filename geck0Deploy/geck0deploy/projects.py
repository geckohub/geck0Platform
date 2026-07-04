from pathlib import Path
from .utils import root

def parse_projects_yaml(path):
    projects = {}
    current = None

    for line in path.read_text().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue

        if line.startswith("  ") and line.strip().endswith(":"):
            current = line.strip().rstrip(":")
            projects[current] = {}
        elif current and line.startswith("    ") and ":" in line:
            key, value = line.strip().split(":", 1)
            projects[current][key.strip()] = value.strip()

    return projects

def main(args):
    registry = root() / "governance" / "projects" / "projects.yaml"

    if not registry.exists():
        print(f"Missing project registry: {registry}")
        return

    projects = parse_projects_yaml(registry)

    print("Geck0verse Project Registry")
    print("===========================")
    print()
    print(f"{'Project':<16} {'Host':<8} {'Status':<14} Path")
    print("-" * 80)

    for name, meta in projects.items():
        host = meta.get("host", "-")
        status = meta.get("status", "-")
        path = meta.get("path", "-")
        exists = "OK" if Path(path).exists() else "MISSING"
        print(f"{name:<16} {host:<8} {status:<14} {path} [{exists}]")

from pathlib import Path
from geck0deploy.core.registry import ensure_default_registry, load_projects


def main(args=None):
    ensure_default_registry()
    projects = load_projects()
    print('Geck0verse Project Registry')
    print('===========================')
    print(f"{'Project':<18} {'Host':<8} {'Status':<14} {'Backup':<8} Path")
    print('-'*90)
    for name, meta in projects.items():
        path = meta.get('path','-')
        exists = 'OK' if Path(path).expanduser().exists() else 'MISSING'
        print(f"{name:<18} {meta.get('host','-'):<8} {meta.get('status','-'):<14} {meta.get('backup','true'):<8} {path} [{exists}]")

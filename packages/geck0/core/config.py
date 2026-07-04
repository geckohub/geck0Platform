from pathlib import Path
import os
import yaml

GECK0_HOME = Path(os.environ.get("GECK0_HOME", Path.home() / "geck0Platform"))

def load_yaml(path, default=None):
    p = GECK0_HOME / path
    if not p.exists():
        return default or {}
    with p.open() as f:
        return yaml.safe_load(f) or {}

def save_yaml(path, data):
    p = GECK0_HOME / path
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w") as f:
        yaml.safe_dump(data, f, sort_keys=False)

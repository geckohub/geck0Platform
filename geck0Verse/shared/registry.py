from pathlib import Path
import yaml
CONFIG_ROOT=Path(__file__).resolve().parents[1]/"config"
def load_yaml(name:str)->dict:
    path=CONFIG_ROOT/name
    return yaml.safe_load(path.read_text()) or {} if path.exists() else {}
def projects()->list[dict]: return load_yaml("projects.yaml").get("projects",[])

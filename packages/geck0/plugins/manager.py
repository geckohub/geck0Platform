from pathlib import Path
import os
import yaml

GECK0_HOME = Path(os.environ.get("GECK0_HOME", Path.home() / "geck0Platform"))

class PluginManager:
    def __init__(self, root=None):
        self.root = Path(root or GECK0_HOME / "plugins")

    def discover(self):
        plugins = []
        for manifest in self.root.rglob("plugin.yaml"):
            try:
                with manifest.open() as f:
                    data = yaml.safe_load(f) or {}
                data["_path"] = str(manifest)
                plugins.append(data)
            except Exception as e:
                plugins.append({"name": "broken-plugin", "error": str(e), "_path": str(manifest)})
        return plugins

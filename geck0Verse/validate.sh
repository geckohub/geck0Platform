#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
python3 -m compileall -q shared services clients
for script in install.sh rollback.sh scripts/*.sh clients/*.sh clients/geck0-remote android/Crumble/bootstrap-wrapper.sh; do bash -n "$script"; done
echo "Shell syntax: OK"
python3 - <<'PY'
from pathlib import Path
import yaml
for name in ('docker-compose.yml','docker-compose.security.yml','config/projects.yaml','config/intents.yaml','config/layers.yaml','config/schedules.yaml'):
    with open(name, encoding='utf-8') as f:
        yaml.safe_load(f)
print('YAML: OK')
required=['README.md','install.sh','services/hub/app.py','android/Crumble/app/build.gradle.kts','dashboard/index.html']
for item in required:
    assert Path(item).exists(), item
print('Required files: OK')
PY
if command -v pytest >/dev/null 2>&1; then
  pytest -q
else
  echo "pytest not installed; Python compile/YAML validation passed"
fi
echo "Validation complete."

#!/usr/bin/env bash

GECK0_HOME="${GECK0_HOME:-$HOME/geck0Platform}"

echo
echo "=============================="
echo "   🦎 GECK0 DEPLOY STATUS"
echo "=============================="
echo

python3 <<PY
import yaml
from pathlib import Path

cfg=Path("$GECK0_HOME/config/devices.yaml")

if not cfg.exists():
    print("devices.yaml not found")
    raise SystemExit

data=yaml.safe_load(cfg.read_text())

for name,dev in data["devices"].items():
    print(f"{name:16}  {dev.get('role','')}")
    if dev.get("host"):
        print(f"   Host : {dev['host']}")
        print(f"   Port : {dev.get('ssh_port',22)}")
    print(f"   Online : {dev.get('online')}")
    print()
PY

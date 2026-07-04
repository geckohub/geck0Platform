# Geck0 Auto-Install / Update Process

## Purpose

Geck0 updates are delivered as ZIP files.

Each update ZIP must contain an `install.sh` file at the root of the ZIP.

The Geck0 Update Watcher automatically detects ZIP files, verifies them, extracts them, runs `install.sh`, logs the result, and moves the ZIP into either `installed/` or `failed/`.

## Main JE Paths

Geck0 home:

```bash
/home/lucy/geck0Platform
```

Update inbox:

```bash
/home/lucy/geck0Platform/updates/incoming
```

Installed updates:

```bash
/home/lucy/geck0Platform/updates/installed
```

Failed updates:

```bash
/home/lucy/geck0Platform/updates/failed
```

Processing folder:

```bash
/home/lucy/geck0Platform/updates/processing
```

Backups:

```bash
/home/lucy/geck0Platform/updates/backups
```

Logs:

```bash
/home/lucy/geck0Platform/updates/logs
```

Watcher script:

```bash
/home/lucy/geck0Platform/scripts/geck0UpdateWatcher.sh
```

Systemd user service:

```bash
/home/lucy/.config/systemd/user/geck0-update-watcher.service
```

## How to Send Updates from Mac

Mac source folder for JelliedEel:

```bash
/Users/phildonachie/Out/Jellied Eel
```

Mac source folder for ThaiGreen:

```bash
/Users/phildonachie/Out/Thai Green
```

Manual Mac trigger:

```bash
geck0send
```

or:

```bash
~/geck0_send_to_pis.sh
```

The Mac sender uses `rsync` over SSH port `1991`.

JelliedEel destination:

```bash
lucy@192.168.1.244:/home/lucy/geck0Platform/updates/incoming/
```

ThaiGreen destination:

```bash
lucy@192.168.1.172:/home/lucy/geck0Platform/updates/incoming/
```

## Update ZIP Rules

Every installable ZIP must have this structure:

```text
update-name.zip
└── install.sh
```

Optional additional files:

```text
update-name.zip
├── install.sh
├── README.md
├── files/
├── config/
├── docs/
└── manifests/
```

The installer runs:

```bash
bash ./install.sh
```

from the extracted ZIP folder.

Inside `install.sh`, use:

```bash
GECK0_HOME="${GECK0_HOME:-$HOME/geck0Platform}"
cd "$GECK0_HOME"
```

## Check Watcher Status

```bash
systemctl --user status geck0-update-watcher.service
```

Expected:

```text
Active: active (running)
```

## Restart Watcher

```bash
systemctl --user restart geck0-update-watcher.service
```

## Watch Logs Live

Systemd logs:

```bash
journalctl --user -u geck0-update-watcher.service -f
```

Geck0 log file:

```bash
tail -f ~/geck0Platform/updates/logs/updateWatcher.log
```

## See Installed Updates

```bash
ls -lh ~/geck0Platform/updates/installed
```

## See Failed Updates

```bash
ls -lh ~/geck0Platform/updates/failed
```

## Read Failed Install Log

Example:

```bash
tail -120 ~/geck0Platform/updates/logs/geck0_foundation_pack_0_1_0_20260701_023347.log
```

## Manual Install for Debugging

```bash
mkdir -p /tmp/geck0_debug_update
unzip ~/geck0Platform/updates/failed/example.zip -d /tmp/geck0_debug_update
cd /tmp/geck0_debug_update
bash ./install.sh
```

## Current Installed Core Updates

Known baseline updates:

- `geck0_first_integration_update`
- `geck0_update_2_crumble_api_service`
- `geck0_voice_pack_1`
- `geck0_foundation_pack_0_1_1`

## Health Checks

Crumble API:

```bash
curl http://localhost:8890/status
curl "http://localhost:8890/search?q=ketama"
```

Voice API:

```bash
curl http://localhost:8891/status
```

Voice diagnostics:

```bash
cd ~/geck0Platform
source .venv/bin/activate
python services/voice/voice_status.py
```

Foundation package test:

```bash
cd ~/geck0Platform
source .venv/bin/activate
PYTHONPATH=packages python3 - <<'PY'
from geck0.plugins.manager import PluginManager
from geck0.search.engine import Geck0Search
print(PluginManager().discover())
print(Geck0Search().search("ketama"))
PY
```

## Recommended Agent Workflow

1. Build update as a ZIP.
2. Ensure `install.sh` is in the root.
3. Put ZIP in Mac folder:
   - `/Users/phildonachie/Out/Jellied Eel`
   - or `/Users/phildonachie/Out/Thai Green`
4. Run:

```bash
geck0send
```

5. On JE, monitor:

```bash
tail -f ~/geck0Platform/updates/logs/updateWatcher.log
```

6. If failed, inspect:

```bash
ls -lt ~/geck0Platform/updates/logs | head
ls -lh ~/geck0Platform/updates/failed
```

7. Patch, rebuild ZIP, resend.

## Safety Notes

The watcher currently auto-runs ZIPs because Phil personally controls the inbox folders.

Future updater v2 should add:

- manifest validation
- version checks
- rollback
- service health checks
- optional package signatures
- dashboard update widget
- Crumble notifications
- Knowledge Graph update event

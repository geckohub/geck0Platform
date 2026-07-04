from __future__ import annotations

import tarfile
from pathlib import Path
from .utils import root, ensure_dir, now_stamp


def package_tg(name: str) -> Path:
    r = root()
    out_dir = r / "governance" / "tg" / "pending_updates"
    ensure_dir(out_dir)
    out = out_dir / f"{now_stamp()}_{name}.tar.gz"
    include = ["geck0Deploy", "governance", "scripts", "config", "api"]
    with tarfile.open(out, "w:gz") as tf:
        for item in include:
            p = r / item
            if p.exists():
                tf.add(p, arcname=item)
    print(f"TG update package created: {out}")
    return out


def write_bootstrap() -> Path:
    r = root()
    boot = r / "governance" / "tg" / "bootstrap" / "geck0_tg_bootstrap.sh"
    ensure_dir(boot.parent)
    boot.write_text(r'''#!/usr/bin/env bash
set -euo pipefail
mkdir -p "$HOME/geck0Platform_tg_updates/incoming" "$HOME/geck0Platform_tg_updates/applied" "$HOME/geck0Platform_tg_updates/logs"
cat > "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail
JE_HOST="lucy@192.168.1.244"
JE_PORT="1991"
REMOTE_DIR="/home/lucy/geck0Platform/governance/tg/pending_updates"
LOCAL_IN="$HOME/geck0Platform_tg_updates/incoming"
LOCAL_APPLIED="$HOME/geck0Platform_tg_updates/applied"
LOG="$HOME/geck0Platform_tg_updates/logs/pull_$(date +%Y%m%d_%H%M%S).log"
mkdir -p "$LOCAL_IN" "$LOCAL_APPLIED" "$(dirname "$LOG")"
rsync -avz -e "ssh -p $JE_PORT" "$JE_HOST:$REMOTE_DIR/" "$LOCAL_IN/" | tee -a "$LOG"
for pkg in "$LOCAL_IN"/*.tar.gz; do
  [ -e "$pkg" ] || continue
  base="$(basename "$pkg")"
  [ -f "$LOCAL_APPLIED/$base.done" ] && echo "Already applied: $base" | tee -a "$LOG" && continue
  tar -xzf "$pkg" -C "$HOME"
  touch "$LOCAL_APPLIED/$base.done"
  echo "Applied: $base" | tee -a "$LOG"
done
EOS
chmod +x "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh"
echo "TG bootstrap complete. Run: ~/geck0Platform_tg_updates/geck0_tg_pull_updates.sh"
''')
    boot.chmod(0o755)
    print(f"Wrote TG bootstrap: {boot}")
    return boot

#!/usr/bin/env bash
set -euo pipefail

echo "Bootstrapping TG Geck0 update system..."

mkdir -p "$HOME/geck0Platform_tg_updates/incoming"
mkdir -p "$HOME/geck0Platform_tg_updates/applied"
mkdir -p "$HOME/geck0Platform_tg_updates/logs"

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

echo "Pulling TG updates from JE..." | tee -a "$LOG"

rsync -avz -e "ssh -p $JE_PORT" \
  "$JE_HOST:$REMOTE_DIR/" \
  "$LOCAL_IN/" | tee -a "$LOG"

for pkg in "$LOCAL_IN"/*.tar.gz; do
  [ -e "$pkg" ] || continue
  base="$(basename "$pkg")"

  if [ -f "$LOCAL_APPLIED/$base.done" ]; then
    echo "Already applied: $base" | tee -a "$LOG"
    continue
  fi

  echo "Applying: $base" | tee -a "$LOG"
  tar -xzf "$pkg" -C "$HOME"

  touch "$LOCAL_APPLIED/$base.done"
  echo "Applied: $base" | tee -a "$LOG"
done

echo "TG update pull complete." | tee -a "$LOG"
EOS

chmod +x "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh"

echo
echo "TG bootstrap complete."
echo "Run updates anytime with:"
echo "$HOME/geck0Platform_tg_updates/geck0_tg_pull_updates.sh"

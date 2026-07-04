#!/usr/bin/env bash
set -euo pipefail

JE_HOST="lucy@192.168.1.244"
JE_PORT="1991"
REMOTE_DIR="/home/lucy/geck0Platform/governance/tg/pending_updates"

BASE="$HOME/geck0Platform_tg_updates"
IN="$BASE/incoming"
EXTRACTED="$BASE/extracted"
APPLIED="$BASE/applied"
LOGDIR="$BASE/logs"
LOG="$LOGDIR/tg_catchup_$(date +%Y%m%d_%H%M%S).log"

mkdir -p "$IN" "$EXTRACTED" "$APPLIED" "$LOGDIR"

echo "=== TG Catch-up started ===" | tee -a "$LOG"
echo "Pulling updates from JE..." | tee -a "$LOG"

rsync -avz -e "ssh -p $JE_PORT" "$JE_HOST:$REMOTE_DIR/" "$IN/" | tee -a "$LOG"

shopt -s nullglob

for pkg in "$IN"/*.zip "$IN"/*.tar.gz; do
  base="$(basename "$pkg")"

  if [ -f "$APPLIED/$base.done" ]; then
    echo "Already applied: $base" | tee -a "$LOG"
    continue
  fi

  echo "Processing: $base" | tee -a "$LOG"

  DEST="$EXTRACTED/${base%.*}"
  mkdir -p "$DEST"

  case "$pkg" in
    *.zip)
      unzip -o "$pkg" -d "$DEST" | tee -a "$LOG"
      ;;
    *.tar.gz)
      tar -xzf "$pkg" -C "$DEST" | tee -a "$LOG"
      ;;
  esac

  if find "$DEST" -maxdepth 3 -type f \( -name "install.sh" -o -name "*.install.sh" -o -name "setup.sh" \) | grep -q .; then
    echo "Installer found. Running installer(s)..." | tee -a "$LOG"
    find "$DEST" -maxdepth 3 -type f \( -name "install.sh" -o -name "*.install.sh" -o -name "setup.sh" \) -print0 |
    while IFS= read -r -d '' installer; do
      chmod +x "$installer"
      bash "$installer" | tee -a "$LOG"
    done
  else
    echo "No installer found. Stored as extracted package/docs." | tee -a "$LOG"
  fi

  touch "$APPLIED/$base.done"
  echo "Applied/recorded: $base" | tee -a "$LOG"
done

echo "=== TG Catch-up complete ===" | tee -a "$LOG"
echo "Incoming:  $IN"
echo "Extracted: $EXTRACTED"
echo "Applied:   $APPLIED"
echo "Logs:      $LOGDIR"

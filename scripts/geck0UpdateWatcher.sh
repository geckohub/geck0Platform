#!/usr/bin/env bash
set -u

GECK0_HOME="$HOME/geck0Platform"
INCOMING="$GECK0_HOME/updates/incoming"
PROCESSING="$GECK0_HOME/updates/processing"
INSTALLED="$GECK0_HOME/updates/installed"
FAILED="$GECK0_HOME/updates/failed"
BACKUPS="$GECK0_HOME/updates/backups"
LOGS="$GECK0_HOME/updates/logs"

mkdir -p "$INCOMING" "$PROCESSING" "$INSTALLED" "$FAILED" "$BACKUPS" "$LOGS"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGS/updateWatcher.log"
}

process_zip() {
  zipfile="$1"
  base="$(basename "$zipfile")"
  stamp="$(date +%Y%m%d_%H%M%S)"
  work="$PROCESSING/${base%.zip}_$stamp"
  logfile="$LOGS/${base%.zip}_$stamp.log"

  log "Detected ZIP: $base"

  mkdir -p "$work"

  # Wait until copy finishes
  sleep 2

  if ! unzip -t "$zipfile" >/dev/null 2>&1; then
    log "FAILED integrity check: $base"
    mv "$zipfile" "$FAILED/${base%.zip}_$stamp.zip"
    return
  fi

  unzip -q "$zipfile" -d "$work"

  if [ ! -f "$work/install.sh" ]; then
    log "FAILED: no install.sh in root of ZIP: $base"
    mv "$zipfile" "$FAILED/${base%.zip}_$stamp.zip"
    rm -rf "$work"
    return
  fi

  chmod +x "$work/install.sh"

  log "Creating backup before install: $base"
  tar -czf "$BACKUPS/geck0Platform_backup_$stamp.tar.gz" \
    --exclude="$GECK0_HOME/updates" \
    -C "$HOME" geck0Platform >/dev/null 2>&1

  log "Running install.sh for $base"

  (
    cd "$work"
    export GECK0_HOME="$GECK0_HOME"
    export UPDATE_WORKDIR="$work"
    bash ./install.sh
  ) >"$logfile" 2>&1

  rc=$?

  if [ "$rc" -eq 0 ]; then
    log "INSTALLED OK: $base"
    mv "$zipfile" "$INSTALLED/${base%.zip}_$stamp.zip"
    rm -rf "$work"
  else
    log "FAILED install rc=$rc: $base"
    mv "$zipfile" "$FAILED/${base%.zip}_$stamp.zip"
    log "See log: $logfile"
  fi
}

log "Geck0 Update Watcher started"
log "Watching: $INCOMING"

while true; do
  for z in "$INCOMING"/*.zip; do
    [ -e "$z" ] || continue
    process_zip "$z"
  done
  sleep 5
done

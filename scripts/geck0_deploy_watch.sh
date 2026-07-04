#!/usr/bin/env bash
set -euo pipefail

BASE="$HOME/geck0Platform"
LOG="$BASE/updates/logs/geck0_deploy_watch.log"

mkdir -p "$BASE/updates"/{incoming/TG,incoming/JE,applied,archive,failed,logs}

echo "[START] Geck0 deploy watcher $(date)" >> "$LOG"

while true; do
  for zip in "$BASE"/updates/incoming/JE/*.zip; do
    [ -e "$zip" ] || continue
    name="$(basename "$zip")"
    stamp="$(date +%Y%m%d_%H%M%S)"

    echo "[JE] Processing $name" >> "$LOG"

    dest="$BASE/updates/applied/${stamp}_${name%.zip}"
    mkdir -p "$dest"

    if unzip -q "$zip" -d "$dest"; then
      mv "$zip" "$BASE/updates/archive/${stamp}_$name"
      echo "[JE] Applied $name to $dest" >> "$LOG"
    else
      mv "$zip" "$BASE/updates/failed/${stamp}_$name"
      echo "[JE] FAILED $name" >> "$LOG"
    fi
  done

  for zip in "$BASE"/updates/incoming/TG/*.zip; do
    [ -e "$zip" ] || continue
    name="$(basename "$zip")"
    echo "[TG] Forwarding $name to ThaiGreen" >> "$LOG"

    scp -P 1991 "$zip" lucy@192.168.1.172:~/geck0Platform/updates/incoming/TG/ \
      && mv "$zip" "$BASE/updates/archive/forwarded_$(date +%Y%m%d_%H%M%S)_$name" \
      || echo "[TG] Forward failed $name" >> "$LOG"
  done

  sleep 10
done

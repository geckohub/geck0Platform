#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/geck0Platform"
DEST="$HOME/geck0_architecture_backups"
DATE="$(date +%Y%m%d_%H%M%S)"
OUT="$DEST/geck0verse_architecture_${DATE}.tar.gz"

mkdir -p "$DEST"

tar \
  --exclude='.git' \
  --exclude='__pycache__' \
  --exclude='*.pyc' \
  --exclude='node_modules' \
  --exclude='.venv' \
  --exclude='venv' \
  --exclude='reports' \
  --exclude='updates' \
  --exclude='storage' \
  --exclude='logs' \
  --exclude='client*' \
  --exclude='clients' \
  --exclude='evidence' \
  --exclude='screenshots' \
  --exclude='*.tar.gz' \
  --exclude='*.zip' \
  --exclude='*.mp4' \
  --exclude='*.mov' \
  --exclude='*.mkv' \
  --exclude='*.iso' \
  -czf "$OUT" \
  -C "$HOME" geck0Platform

echo "Created architecture backup:"
ls -lh "$OUT"

#!/usr/bin/env bash
set -euo pipefail

NAME="${1:-tg_update}"
DATE="$(date +%Y%m%d_%H%M%S)"
ROOT="$HOME/geck0Platform"
OUT="$ROOT/governance/tg/pending_updates/${DATE}_${NAME}.tar.gz"

tar \
  --exclude='.git' \
  --exclude='logs' \
  --exclude='reports' \
  --exclude='storage' \
  --exclude='node_modules' \
  --exclude='.venv' \
  --exclude='venv' \
  -czf "$OUT" \
  -C "$ROOT" geck0Docs scripts api config governance

echo "TG update package created:"
ls -lh "$OUT"

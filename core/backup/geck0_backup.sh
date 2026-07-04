#!/usr/bin/env bash
set -euo pipefail
ROOT="$HOME/geck0Platform"; OUT="$ROOT/backups/geck0_backup_$(date +%Y%m%d_%H%M%S).tar.gz"
mkdir -p "$ROOT/backups"
tar --exclude="$ROOT/backups" --exclude="$ROOT/updates/work" -czf "$OUT" "$ROOT" 2>/dev/null || true
echo "✅ Backup created: $OUT"
if [ -n "${LINODE_BACKUP_TARGET:-}" ]; then rsync -av "$OUT" "$LINODE_BACKUP_TARGET"; fi

#!/usr/bin/env bash
set -e
STAMP=$(date +%Y%m%d_%H%M%S)
ARCH="$HOME/archive/ph0enix_cleanup_$STAMP"
mkdir -p "$ARCH"
echo "🧹 Safe cleanup. Archiving loose old scripts/logs to $ARCH"
# Only archive loose home-level scripts/logs, never project folders.
find "$HOME" -maxdepth 1 -type f \( -name '*.sh' -o -name '*.log' -o -name '*.bak' -o -name '*~' \) -print -exec mv {} "$ARCH" \; 2>/dev/null || true
# Retire failed duplicate zip attempts older than today if any.
mkdir -p "$HOME/geck0Platform/updates/retired"
find "$HOME/geck0Platform/updates/failed" -type f -name '*.zip' -mtime +1 -print -exec mv {} "$HOME/geck0Platform/updates/retired/" \; 2>/dev/null || true
tar -czf "$ARCH.tar.gz" -C "$(dirname "$ARCH")" "$(basename "$ARCH")"
echo "✅ Cleanup archive: $ARCH.tar.gz"

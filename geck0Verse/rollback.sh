#!/usr/bin/env bash
set -euo pipefail
SNAPSHOT="${1:-}"
DEST="${GECK0_PLATFORM_ROOT:-$HOME/geck0Platform}/geck0Verse"
if [ -z "$SNAPSHOT" ] || [ ! -d "$SNAPSHOT" ]; then
  echo "Usage: $0 /path/to/geck0Verse_snapshot" >&2
  exit 2
fi
mv "$DEST" "${DEST}.failed.$(date +%Y%m%d_%H%M%S)" 2>/dev/null || true
cp -a "$SNAPSHOT" "$DEST"
echo "Restored $DEST from $SNAPSHOT"

#!/usr/bin/env bash
set -euo pipefail
ROOT="$HOME/geck0Platform"; IN="$ROOT/updates/incoming"; AP="$ROOT/updates/applied"; WK="$ROOT/updates/work"
mkdir -p "$IN" "$AP" "$WK" "$ROOT/updates/retired_broken"
# retire known broken early packs
mv "$IN"/Geck0_Universal_Command_Centre_v0_*.zip "$ROOT/updates/retired_broken/" 2>/dev/null || true
mv "$IN"/Geck0_Foundation_v1_0.zip "$ROOT/updates/retired_broken/" 2>/dev/null || true
echo '🦎 GECK0 UPDATE — pending ZIPs oldest first'
find "$IN" -type f -name '*.zip' -printf '%T@ %p\n' | sort -n | while read -r _ zip; do
  base=$(basename "$zip"); marker="$AP/$base.applied"; [ -f "$marker" ] && { echo "⏭️ $base"; continue; }
  echo "📦 $base"; rm -rf "$WK/current"; mkdir -p "$WK/current"; unzip -q "$zip" -d "$WK/current"
  inst=$(find "$WK/current" -name install_on_je.sh | head -1 || true); [ -z "$inst" ] && { echo "⚠️ no installer"; continue; }
  (cd "$(dirname "$inst")" && bash ./install_on_je.sh); date > "$marker"; echo "✅ $base"
done

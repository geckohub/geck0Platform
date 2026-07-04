#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
DEST="$HOME/geck0Platform"
mkdir -p "$DEST/geck0Deploy"
cp -a "$SRC/geck0Deploy/." "$DEST/geck0Deploy/"
chmod +x "$DEST/geck0Deploy/bin/geck0" "$DEST/geck0Deploy/bin/geck0-py"
mkdir -p "$DEST/governance/tg/pending_updates" "$DEST/governance/projects"
if [ ! -f "$DEST/governance/projects/projects.yaml" ]; then
cat > "$DEST/governance/projects/projects.yaml" <<EOR
projects:
  geck0Platform:
    path: $DEST
    family: geck0
    status: active
    host: JE
    backup: true
EOR
fi
if [ -f "$HOME/.bashrc" ]; then
  grep -q 'geck0Platform/geck0Deploy/bin' "$HOME/.bashrc" || echo 'export PATH="$HOME/geck0Platform/geck0Deploy/bin:$PATH"' >> "$HOME/.bashrc"
fi
if [ -f "$HOME/.zshrc" ]; then
  grep -q 'geck0Platform/geck0Deploy/bin' "$HOME/.zshrc" || echo 'export PATH="$HOME/geck0Platform/geck0Deploy/bin:$PATH"' >> "$HOME/.zshrc"
fi
echo "Installed Geck0Deploy v1.0 into $DEST"
echo "Run: source ~/.bashrc && geck0 help"

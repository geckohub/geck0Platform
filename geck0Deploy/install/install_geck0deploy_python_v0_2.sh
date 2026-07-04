#!/usr/bin/env bash
set -euo pipefail
ROOT="${GECK0_ROOT:-$HOME/geck0Platform}"
SRC_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"

echo "Installing Geck0Deploy Python v0.2 into: $ROOT"
mkdir -p "$ROOT"
rsync -av "$SRC_DIR/geck0Deploy/" "$ROOT/geck0Deploy/"
chmod +x "$ROOT/geck0Deploy/bin/geck0-py"

if ! grep -q 'geck0Deploy/bin' "$HOME/.bashrc" 2>/dev/null; then
  echo 'export PATH="$HOME/geck0Platform/geck0Deploy/bin:$PATH"' >> "$HOME/.bashrc"
fi

mkdir -p "$ROOT/governance/tg/pending_updates" "$ROOT/governance/tg/bootstrap" "$ROOT/governance/backups"

echo
echo "Installed. Test with:"
echo "  source ~/.bashrc"
echo "  geck0-py verify"
echo
echo "Optional commands:"
echo "  geck0-py tg-bootstrap"
echo "  geck0-py package-tg geck0deploy_python_v0_2"
echo "  geck0-py release geck0deploy_python_v0_2"

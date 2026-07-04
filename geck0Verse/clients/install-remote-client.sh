#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)/geck0-remote"
DEST="$HOME/.local/bin"
mkdir -p "$DEST"
cp "$SRC" "$DEST/geck0-remote"
chmod +x "$DEST/geck0-remote"
for name in geck0 ped0na m0nkey li0n; do ln -sfn "$DEST/geck0-remote" "$DEST/$name"; done
shell_rc="$HOME/.bashrc"; [ -n "${ZSH_VERSION:-}" ] && shell_rc="$HOME/.zshrc"
grep -q '\.local/bin' "$shell_rc" 2>/dev/null || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$shell_rc"
echo "Installed remote launchers. Reload your shell, then run: geck0 help"

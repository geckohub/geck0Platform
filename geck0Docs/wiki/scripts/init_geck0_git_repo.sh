#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${1:-$HOME/geck0Platform}"
cd "$REPO_DIR"

if [ ! -d .git ]; then
  git init
fi

git add .
git commit -m "Initial Geck0 platform archive and wiki foundation" || true

echo "[+] Git repo ready at $REPO_DIR"
echo "[+] Next: create a remote repo and run:"
echo "    git remote add origin <your-repo-url>"
echo "    git branch -M main"
echo "    git push -u origin main"

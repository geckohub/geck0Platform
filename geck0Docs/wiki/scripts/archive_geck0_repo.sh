#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="${1:-$HOME/geck0Platform}"
STAMP="$(date +%Y%m%d_%H%M%S)"
ARCHIVE_DIR="$HOME/geck0_archives"
ARCHIVE_NAME="geck0Platform_archive_${STAMP}.tar.gz"

mkdir -p "$ARCHIVE_DIR"

echo "[+] Archiving $REPO_DIR"
tar --exclude='.git' --exclude='node_modules' --exclude='__pycache__' --exclude='.venv' -czf "$ARCHIVE_DIR/$ARCHIVE_NAME" -C "$(dirname "$REPO_DIR")" "$(basename "$REPO_DIR")"

echo "[+] Archive created: $ARCHIVE_DIR/$ARCHIVE_NAME"

#!/usr/bin/env bash
set -euo pipefail

LOCAL_DIR="$HOME/geck0_architecture_backups"
LINODE_USER="pinkgeck0"
LINODE_HOST="172.233.15.159"
LINODE_DIR="/home/pinkgeck0/backups/software_architecture"

"$HOME/geck0Platform/governance/scripts/geck0_architecture_backup.sh"

LATEST="$(ls -t "$LOCAL_DIR"/geck0verse_architecture_*.tar.gz | head -n 1)"

ssh "$LINODE_USER@$LINODE_HOST" "mkdir -p '$LINODE_DIR'"
scp "$LATEST" "$LINODE_USER@$LINODE_HOST:$LINODE_DIR/"

echo "Uploaded to Linode:"
echo "$LATEST"

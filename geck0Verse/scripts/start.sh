#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker compose up -d --build
echo "Dashboard: http://$(hostname -I | awk '{print $1}'):8088"

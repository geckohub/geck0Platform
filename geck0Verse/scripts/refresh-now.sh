#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
TOKEN="$(grep '^GECK0_API_TOKEN=' .env | cut -d= -f2-)"
curl -fsS -X POST -H "X-Geck0-Token: $TOKEN" http://localhost:8101/v1/refresh; echo
curl -fsS -X POST -H "X-Geck0-Token: $TOKEN" http://localhost:8102/v1/refresh; echo

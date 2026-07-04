#!/usr/bin/env bash
set -euo pipefail
for url in \
  http://localhost:8080/health \
  http://localhost:8101/health \
  http://localhost:8102/health \
  http://localhost:8103/health \
  http://localhost:8104/health \
  http://localhost:8110/health; do
  printf '%-40s ' "$url"
  curl -fsS "$url" >/dev/null && echo OK || echo FAIL
done

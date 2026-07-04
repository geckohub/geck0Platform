#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
grep "^GECK0_API_TOKEN=" .env | cut -d= -f2-

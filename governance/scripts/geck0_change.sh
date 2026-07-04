#!/usr/bin/env bash
set -euo pipefail

ROOT="$HOME/geck0Platform"
DATE="$(date +%Y-%m-%d_%H-%M-%S)"
PROJECT="${1:-general}"
TITLE="${2:-untitled-change}"

mkdir -p "$ROOT/governance/change_control/$PROJECT"
mkdir -p "$ROOT/governance/release_notes/$PROJECT"
mkdir -p "$ROOT/governance/wiki/$PROJECT"

CHANGE_FILE="$ROOT/governance/change_control/$PROJECT/${DATE}_${TITLE}.md"

cat > "$CHANGE_FILE" <<EON
# Change Record: $TITLE

Date: $DATE  
Project: $PROJECT  
Host: $(hostname)

## Summary

TODO

## Files Changed

TODO

## Reason

TODO

## Test Notes

TODO

## Release Note

TODO

## Wiki Update Needed?

- [ ] Yes
- [ ] No

## Backup/Deploy Impact

TODO
EON

echo "Created: $CHANGE_FILE"

#!/usr/bin/env bash
set -e

GP="$HOME/geck0Platform"

echo "## 🩺 Doctor's Prescription"
echo
echo "### Git changes"
for repo in "$HOME/geck0" "$HOME/geck0Platform" "$HOME/ph0enix"; do
  if [ -d "$repo/.git" ]; then
    echo
    echo "#### $repo"
    git -C "$repo" status --short || true
    git -C "$repo" log --oneline -5 || true
  fi
done

echo
echo "### Major alerts / failures"
find "$GP/updates/failed" -type f 2>/dev/null | tail -20 || true
docker ps -a --filter "status=exited" --format '- {{.Names}} {{.Status}}' 2>/dev/null || true
journalctl -p 3 -n 20 --no-pager 2>/dev/null || true

echo
echo "### Recommended priorities"
echo "1. Review failed update packages."
echo "2. Check exited Docker containers."
echo "3. Review disk usage and archive old logs."
echo "4. Confirm API keys are present."
echo "5. Commit any meaningful code/wiki changes."

echo
echo "### Suggested medicine"
echo
echo '```bash'
echo 'geck0 backup full'
echo 'geck0 doctor apply safe'
echo 'geck0 clean logs'
echo 'geck0 update retry'
echo 'git -C ~/geck0Platform status'
echo '```'

echo
echo "### Approval model"
echo "No destructive remediation should run automatically."
echo "Run doctor apply only after backup and review."

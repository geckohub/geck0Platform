#!/usr/bin/env bash
GECK0_HOME="$HOME/geck0Platform"
echo
echo "Installed Geck0 plugins:"
echo
find "$GECK0_HOME/plugins" "$GECK0_HOME/folders" -name plugin.yaml -o -name plugin.yml 2>/dev/null | sort
echo

#!/usr/bin/env bash
GECK0_HOME="$HOME/geck0Platform"
echo
echo "Geck0verse status"
echo "Root: $GECK0_HOME"
echo
tree -L 1 "$GECK0_HOME" 2>/dev/null || ls -la "$GECK0_HOME"
echo

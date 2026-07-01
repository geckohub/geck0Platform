#!/usr/bin/env bash
GECK0_HOME="$HOME/geck0Platform"
git -C "$GECK0_HOME" ${*:-status}

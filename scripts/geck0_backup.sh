#!/usr/bin/env bash
set -e
GP="$HOME/geck0Platform"; mode="${1:-full}"; out="$GP/backups/geck0_${mode}_$(date +%Y%m%d_%H%M%S).tar.gz"; mkdir -p "$GP/backups"; tar -czf "$out" "$GP/wiki" "$GP/registry" "$GP/config" "$GP/reports" 2>/dev/null || true; echo "$out"

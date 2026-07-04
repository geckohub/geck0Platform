#!/usr/bin/env bash
GP="$HOME/geck0Platform"; ok=0; checks=0
echo "🩺 Geck0/Ph0enix Doctor v4"
for d in "$GP" "$GP/registry" "$GP/wiki" "$GP/config" "$GP/dashboards" "$GP/updates" "$GP/reports"; do checks=$((checks+1)); [ -d "$d" ] && { echo "✅ $d"; ok=$((ok+1)); } || echo "⚠️ missing $d"; done
for c in geck0 ph0enix fusebox crumble ped0na m0nkey li0n breadcrumbs geck0earth chipyard geck0play shopbot; do checks=$((checks+1)); command -v "$c" >/dev/null && { echo "✅ cmd:$c"; ok=$((ok+1)); } || echo "⚠️ cmd:$c missing"; done
echo "Summary: $ok / $checks checks OK"

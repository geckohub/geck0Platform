#!/usr/bin/env bash

GECK0_HOME="$HOME/geck0Platform"
COMMAND_DIR="$GECK0_HOME/core/commands"

clear
echo "#############################################################"
echo "              🦎  G E C K 0 V E R S E"
echo "                    Geck0 Shell / gsh"
echo "#############################################################"
echo
echo "Type: help, menu, plugins, status, clear, q, x"
echo

while true; do
  read -rp "Geck0> " line
  cmd="$(echo "$line" | awk '{print $1}')"
  args="${line#"$cmd"}"
  args="${args# }"

  case "$cmd" in
    q|Q|x|X|exit|quit) exit 0 ;;
    clear|cls) clear ;;
    help|h) echo "Commands: help menu plugins status scan search crumble cyberx dashboard wiki git report" ;;
    menu|m) echo "Menu: Crumble | CyberX | BlackGeck0 | GreenGeck0 | PinkGeck0 | BlueGeck0 | YellowGeck0 | PurpleGeck0 | Search | Dashboard | Wiki | Git" ;;
    plugins) find "$GECK0_HOME/plugins" "$GECK0_HOME/folders" \( -name plugin.yaml -o -name plugin.yml \) 2>/dev/null | sort ;;
    status) echo "Root: $GECK0_HOME"; tree -L 1 "$GECK0_HOME" 2>/dev/null || ls -la "$GECK0_HOME" ;;
    git) git -C "$GECK0_HOME" ${args:-status} ;;
    "") ;;
    *) echo "Command placeholder: $cmd $args" ;;
  esac
done

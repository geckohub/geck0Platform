# Geck0 Shell and Plugin System

## Geck0 Shell

`geck0` launches the Geck0verse shell.

Alias:

`gsh`

## Purpose

The shell is the command interface for Geck0verse.

It supports:
- Commands
- Menus
- Plugins
- Crumble
- CyberX
- Geck0 Search
- Dashboard actions
- Wiki/Git/API shortcuts

## Command Style

Examples:

scan mmcy.uk
search ketama
notes
photos brighton
translate hello german
remind me tomorrow
dashboard
wiki
git status

## Plugin System

Each module can expose a `plugin.yaml`.

Plugin fields:
- name
- command
- description
- menu
- permissions
- entrypoint
- enabled

## Standard Controls

q = quit/back
x = exit
h = help
m = menu
s = search
r = refresh
l = logs

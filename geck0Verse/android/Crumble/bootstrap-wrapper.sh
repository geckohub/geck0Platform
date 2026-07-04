#!/usr/bin/env bash
set -euo pipefail
command -v gradle >/dev/null || { echo "Install Gradle or let Android Studio sync the project first."; exit 1; }
gradle wrapper --gradle-version 9.4.1

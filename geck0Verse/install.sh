#!/usr/bin/env bash
set -euo pipefail
SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${GECK0_PLATFORM_ROOT:-$HOME/geck0Platform}/geck0Verse"
BACKUP_ROOT="${GECK0_PLATFORM_ROOT:-$HOME/geck0Platform}/backups/geck0verse_install"
STAMP="$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_ROOT"
if [ -d "$DEST" ]; then
  cp -a "$DEST" "$BACKUP_ROOT/geck0Verse_$STAMP"
  echo "Existing install backed up to $BACKUP_ROOT/geck0Verse_$STAMP"
fi
mkdir -p "$DEST"
cp -a "$SRC"/. "$DEST"/
rm -rf "$DEST/.git" 2>/dev/null || true
cd "$DEST"
if [ ! -f .env ]; then
  cp .env.example .env
  API_TOKEN="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
  INTERNAL_TOKEN="$(python3 -c 'import secrets; print(secrets.token_urlsafe(32))')"
  DB_PASS="$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')"
  FERNET="$(python3 -c 'import os,base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode())')"
  sed -i "s/GECK0_API_TOKEN=CHANGE_ME_GENERATED_BY_INSTALLER/GECK0_API_TOKEN=$API_TOKEN/" .env
  sed -i "s/GECK0_INTERNAL_TOKEN=CHANGE_ME_GENERATED_BY_INSTALLER/GECK0_INTERNAL_TOKEN=$INTERNAL_TOKEN/" .env
  sed -i "s/GECK0_FERNET_KEY=CHANGE_ME_GENERATED_BY_INSTALLER/GECK0_FERNET_KEY=$FERNET/" .env
  sed -i "s/POSTGRES_PASSWORD=CHANGE_ME_GENERATED_BY_INSTALLER/POSTGRES_PASSWORD=$DB_PASS/" .env
  sed -i "s#DATABASE_URL=postgresql+psycopg://geck0:CHANGE_ME_GENERATED_BY_INSTALLER@postgres:5432/geck0verse#DATABASE_URL=postgresql+psycopg://geck0:$DB_PASS@postgres:5432/geck0verse#" .env
  chmod 600 .env
fi
mkdir -p data/{hub/uploads,travelsheep,sealife/import,geck0earth,greengeck0,reports,purplegeck0,bluegeck0,yellowgeck0,pinkgeck0,scheduler,security}
chmod +x validate.sh rollback.sh scripts/*.sh 2>/dev/null || true
./validate.sh
printf '\nInstalled to %s\nNext: cd %s && sudo docker compose up -d --build\n' "$DEST" "$DEST"

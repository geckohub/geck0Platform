# Install on JE

```bash
cd ~
unzip -o geck0verse_integrated_v2_0.zip
cd geck0verse_integrated_v2_0_pkg
./validate.sh
./install.sh
cd ~/geck0Platform/geck0Verse
cp .env.example .env   # installer normally creates this automatically
nano .env              # add optional API keys
sudo docker compose up -d --build
```

Open:

- Dashboard: `http://JE_IP:8088`
- Crumble/Hub API docs: `http://JE_IP:8080/docs`
- TravelSheep: `http://JE_IP:8101/docs`
- SeaLife: `http://JE_IP:8102/docs`
- Geck0Earth: `http://JE_IP:8103/docs`
- Green Geck0: `http://JE_IP:8104/docs`

## Android

Open `android/Crumble` in Android Studio. Set the JE Hub URL and token in the app's Settings
screen. For local development the default base URL is `http://192.168.1.244:8080/`.

## Rollback

The installer snapshots any existing `~/geck0Platform/geck0Verse` directory under
`~/geck0Platform/backups/geck0verse_install/`. Use `./rollback.sh <snapshot-directory>`.

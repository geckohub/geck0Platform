# Geck0Air Wigle Ingest

Download a Wigle CSV export, copy it to JE, then run:

```bash
wigle-ingest /path/to/wigle_export.csv
```

Outputs:
- SQLite rows in `~/geck0Platform/knowledge/geck0_knowledge.db`
- GeoJSON layer in `~/geck0Platform/apps/geck0earth/data/geojson/wigle_latest.geojson`

Use passive/authorised collection only. Avoid overclaiming identity from MAC/Bluetooth/Wi-Fi observations.

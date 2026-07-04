# Geck0verse Integrated Control Plane v2.0

A Docker-first, JE-hosted control plane connecting Crumble, TravelSheep, SeaLife,
Geck0Earth, Green Geck0, BreadCrumbs, Blue/Yellow/Pink/Purple Geck0, and optional
Black Geck0 defensive monitoring components.

## What works without API keys

- Crumble text chat, deterministic intents, query history, suggestions, uploads and domain launcher
- TravelSheep sample UK weekend deals, filtering, map data and manual/automatic refresh
- SeaLife sample Brighton/Hastings/Margate rentals and ownership equivalents, filtering and map data
- Geck0Earth live Open-Meteo weather/air-quality layers plus sample telemetry/observation ingestion
- Green Geck0 safe URL checks and JSON/HTML reports
- BreadCrumbs safe project/repository initialization inside its managed workspace
- Blue/Yellow/Pink/Purple domain APIs and mobile-ready dashboard
- Thursday 02:00 TravelSheep refresh and daily 11:00 SeaLife refresh (Europe/London)

## Optional API connectors

- Open-Meteo: weather, air quality and marine data; no key required for suitable use
- Ticketmaster Discovery API: events near a destination
- Amadeus Self-Service APIs: flight/hotel adapters (credentials required)
- Generic TravelSheep/SeaLife JSON feeds and SeaLife CSV imports
- Ollama on JE for local LLM-assisted Crumble responses

## Important boundaries

- Property portals often do not provide unrestricted public listing APIs. SeaLife ships with
  sample data and lawful JSON/CSV adapter points rather than scraping protected portals.
- Green Geck0 v2 performs low-impact, defensive checks only. Intrusive security testing remains
  separate on authorised TG/GeckoScan workflows.
- Black Geck0 monitoring profiles are opt-in because packet capture and SIEM tooling can be
  resource intensive on a Raspberry Pi.

See `INSTALL.md`, then run `./validate.sh` before installation.

## Daily commands

```bash
./scripts/start.sh
./scripts/status.sh
./scripts/show-token.sh
./scripts/refresh-now.sh
```

Install `clients/geck0-remote` for SSH-based Geck0Deploy commands, or use `clients/crumblectl.py` for direct Crumble API access.

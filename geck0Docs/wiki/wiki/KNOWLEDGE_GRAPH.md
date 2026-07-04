# Geck0 Knowledge Graph

## Purpose

The Geck0 Knowledge Graph is the shared intelligence layer for the ecosystem.

It prevents every project from storing isolated, incompatible data.

## Core idea

Everything becomes an observation.

Examples:
- A port is open.
- A Wi-Fi network was seen.
- A bus stop exists.
- A flight passed overhead.
- A shop closes at midnight.
- A historical event happened here.
- A sensor measured poor air quality.
- A person asked Crumble a question.

## Minimal observation model

Fields:
- id
- source_project
- source_plugin
- observation_type
- title
- description
- timestamp_start
- timestamp_end
- latitude
- longitude
- geometry
- confidence
- raw_payload
- tags
- relationships

## Recommended storage

- PostgreSQL
- PostGIS
- JSONB for raw payloads
- optional graph layer later
- embeddings/vector search later

## Projects that should use it

- Geck0 Earth
- GeckoScan
- Geck0 Air
- Geck0 Radio
- Crumble
- BreadCrumbs
- TravelSheep
- SeaLife
- Pulse
- RobotRainforest

## Next tasks

1. Create common observation schema.
2. Add ingest API.
3. Add query API.
4. Add source/plugin registry.
5. Add dashboard explorer.
6. Add Crumble natural language query layer.

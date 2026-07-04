# Crumble Development Notes

## Vision

Crumble is the conversational and voice interface for the whole Geck0 ecosystem.

Wake phrase: Hey Crumble.

## Roles

- local assistant
- voice command layer
- AI router
- Geck0 project controller
- Home Assistant bridge
- map/query guide for Geck0 Earth
- GeckoScan operator
- BreadCrumbs creative assistant

## Target devices

- JelliedEel Pi 5
- ThaiGreen Pi 5
- Android app
- Pixel Watch / wearable ideas
- LILYGO S3 watch
- Bluetooth speaker/mic nodes
- ESP32 mesh nodes
- smart mirror
- Cyber Harness

## Core functions

- text query path first
- voice later
- local Ollama models
- online fallback where useful
- command routing
- permissions/safety
- Home Assistant integration
- dashboard integration
- journal/memory queries

## Example commands

- Crumble, start a GeckoScan against authorised target.
- Crumble, show me the latest scan results.
- Crumble, show Geck0 Earth local mode.
- Crumble, find a pub still open near me.
- Crumble, make an Alternative Timelines video about dinosaurs surviving.
- Crumble, what planes are overhead?

## Next development tasks

1. Create FastAPI command router.
2. Add local model routing.
3. Add command registry.
4. Add permissions model.
5. Add GeckoScan connector.
6. Add Geck0 Earth connector.
7. Add BreadCrumbs connector.
8. Add Android app endpoint.
9. Add voice input/output later.

# GeckoScan Development Notes

## Vision

GeckoScan evolves from a scanner into the Black Geck0 Security Intelligence Platform.

High-level flow:

Recon -> Knowledge -> Validation -> Reporting -> Autonomous Security Analyst

## Phases

### Phase 1: GeckoScan
Reconnaissance, discovery, asset inventory, telemetry, screenshots, evidence capture, database ingestion, blue-team indicators, Crumble context.

### Phase 2: GeckoExploit
Controlled authorised validation that consumes GeckoScan data and produces validated findings, evidence, and exploitation proof where appropriate.

### Phase 3: GeckoReport
Client-facing deliverable and sellable reporting product.

## Architecture principles

- Plugin-driven collectors
- Per-plugin manifests
- Normalised observations
- PostgreSQL intelligence store
- Historical diff engine
- Relationship graph
- Risk scoring
- API-first dashboard integration
- Crumble voice/text control

## Desired pipeline

Collectors -> Parsers -> Normalised Observations -> PostgreSQL -> Graph -> Scoring -> Reports -> Crumble / Dashboard

## Key features to track

- Resume mode
- Retry queue
- tmux/walkaway mode
- auto-kill hung tools
- screenshots/HTML/headers evidence
- nuclei/nmap/whatweb/httpx/katana/gowitness integration
- WAF/IDS/IPS/SIEM detection notes
- blue-team indicators
- tool_summary.json per tool
- scan diffs
- evidence ZIPs
- API for dashboard and Crumble

## Next development tasks

1. Split large scripts into modules.
2. Create plugin manifest format.
3. Normalise all tool output into observations.
4. Add scan status API.
5. Add Crumble commands:
   - start scan
   - scan status
   - latest findings
   - show evidence
6. Add Geck0 Earth integration:
   - map targets
   - show exposed services geographically where meaningful
   - show infrastructure relationship graph
7. Add GeckoReport renderer.

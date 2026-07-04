# Codex Handoff Guide

## Goal

Create a clean Git repository that Codex can inspect, modify, test, and improve iteratively.

## Before using Codex

1. Archive current Geck0 state.
2. Commit all current files.
3. Add this wiki package.
4. Add roadmap and manifest.
5. Push to a private Git repo or make available locally to Codex CLI.

## Recommended repo structure

```text
geck0Platform/
├── apps/
├── api/
├── core/
├── dashboards/
├── geck0Docs/
│   └── wiki/
├── scripts/
├── updates/
├── storage/
├── README.md
├── ROADMAP.md
└── CODEX.md
```

## Codex working rules

Create a `CODEX.md` file at the repo root containing:

```markdown
# Codex Instructions for Geck0

You are working on the Geck0 ecosystem.

Rules:
- Prefer modular code.
- Do not delete existing working scripts without archiving.
- Add tests for new functionality.
- Add or update wiki docs for every major change.
- Use manifests for plugins and updates.
- Keep JelliedEel and ThaiGreen roles separate.
- Never run destructive commands without explicit confirmation.
- Treat GeckoScan as authorised-security tooling only.
- Keep Geck0 Earth plugins modular and toggleable.
- Make changes in small commits.
```

## First Codex prompt

```text
Read the entire repository and the geck0Docs/wiki folder. Summarise the current architecture, identify duplicate or legacy files, and propose a safe modularisation plan. Do not modify code yet.
```

## Second Codex prompt

```text
Create a docs-only branch update that adds the Geck0 Earth, Crumble, GeckoScan, BreadCrumbs, Geck0 Air/Radio, and Knowledge Graph wiki pages into the correct docs location. Update README and ROADMAP. Add CODEX.md with project rules.
```

## Third Codex prompt

```text
Build the Geck0 Earth v1 foundation as a modular FastAPI + web frontend app with plugin registry, layer manager, timeline engine, mock data plugins, and docs. Keep it runnable with Docker Compose and add tests.
```

## Fourth Codex prompt

```text
Connect Crumble to Geck0 Earth with a simple text query endpoint. Add example commands for local mode, UK mode, and global mode. Use mock responses first.
```

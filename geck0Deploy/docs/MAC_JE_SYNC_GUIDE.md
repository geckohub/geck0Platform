# Mac ↔ JE Git Sync Guide

## Purpose

This document describes the standard Git workflow for the Geck0 Platform.

### Roles

* **JE (JelliedEel)** — Primary development, infrastructure, automation, builds, releases, documentation, backups and deployment.
* **Mac** — Development workstation, editing, testing and administration.
* **GitHub** — Central source of truth for source code and documentation.
* **TG (ThaiGreen)** — Security platform that receives deployment/update packages from JE when online.

---

# Repository

Always use:

```bash
git@github.com:geckohub/geck0Platform.git
```

---

# Before starting work

Always begin by updating your local copy:

```bash
cd ~/geck0Platform
git pull
```

---

# After making changes

```bash
git status
git add .
git commit -m "Describe your changes"
git push
```

---

# On JE

Useful commands:

```bash
geck0 status
geck0 verify
```

Create a release:

```bash
geck0 release my_release_name
```

Create a TG update package:

```bash
geck0 package-tg my_update
```

Create an architecture backup:

```bash
geck0 backup
```

Upload the latest architecture backup to Linode:

```bash
geck0 backup-linode
```

---

# On Mac

Update your local copy:

```bash
cd ~/geck0Platform
git pull
```

Check status:

```bash
git status
```

---

# TG Workflow

TG may be offline for long periods.

JE stores all pending TG deployment packages in:

```text
governance/tg/pending_updates/
```

When TG returns online:

1. Run the bootstrap script (first time only).
2. Run the TG pull script.
3. TG downloads and applies any pending packages.
4. Applied packages are recorded locally on TG.

---

# Weekly Maintenance

* Run `geck0 verify`
* Push completed work to GitHub
* Ensure architecture backups complete successfully
* Check pending TG update queue
* Review release notes and change log

---

# Golden Rules

* JE is the primary infrastructure host.
* GitHub is the canonical source for code and documentation.
* TG is updated from JE and may operate offline.
* Every significant change should include:

  * Change Control
  * Release Notes
  * Wiki Updates
  * Manifest Updates
  * Build Guide Updates
  * Architecture Snapshot
* Keep large client files, evidence, logs and generated artefacts out of the main repository and architecture backups.

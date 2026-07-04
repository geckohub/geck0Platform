# Ped0na Governance and Continuous Improvement Architecture

**Status:** Approved architecture direction  
**Scope:** Ped0na, Geck0, M0nkey, Li0n and all managed applications  
**Primary control plane:** JelliedEel  
**Remote execution node:** ThaiGreen  
**Cloud recovery target:** Linode  
**Conversational interface:** Crumble  
**Observability and analysis:** Shepherd Pie  
**Lifecycle manager:** Geck0Deploy  

---

## 1. Vision

Ped0na is the common umbrella for Geck0, M0nkey and Li0n.

The platform must make personal, professional, client and public systems manageable, documented, observable, actionable, secure, testable, recoverable and enjoyable to use.

The governing loop is:

```text
Observe
→ Understand
→ Recommend
→ Human approval
→ Build
→ Test
→ Document
→ Human deployment approval
→ Deploy
→ Verify
→ Learn
```

No substantial build or deployment should occur automatically without human approval.

---

## 2. Domain Responsibilities

### Ped0na

Ped0na defines shared governance, identity, permissions, workspace separation, lifecycle standards, documentation rules, data boundaries and approvals.

### Geck0

Geck0 provides infrastructure, intelligence, security, deployment, data collection, testing, reporting and operational tooling.

### M0nkey

M0nkey provides workflows, orchestration, automation, repeatable tasks and adaptable operational processes.

### Li0n

Li0n provides oversight, review, prioritisation, recommendations and higher-level decision support.

### Crumble

Crumble provides conversational access, natural-language commands, voice interaction, mobile access, explanations, alerts, suggestions and controlled memory.

---

## 3. Accountability and Audit

Every meaningful action must generate a structured audit event.

Each event should include:

- event ID;
- timestamp and timezone;
- actor;
- source device;
- workspace;
- application;
- intent or command;
- redacted parameters;
- request ID;
- job ID;
- risk classification;
- approval status;
- result and exit code;
- duration;
- affected systems;
- Git commit;
- release version;
- rollback point;
- evidence and report links.

Audit records should be append-only. Operational logs may rotate according to policy, but audit records must not be silently rewritten.

---

## 4. Shepherd Pie

Shepherd Pie is the shared log, event, telemetry and analysis platform.

It should ingest structured data from:

- JelliedEel;
- ThaiGreen;
- Docker;
- Crumble;
- Geck0Deploy;
- TravelSheep;
- SeaLife;
- Geck0Earth;
- Green Geck0;
- BreadCrumbs;
- Blue, Yellow, Pink and Purple Geck0;
- Black Geck0 defensive services;
- Home Assistant;
- Chip Yard;
- Android devices;
- remote launchers.

Recommended flow:

```text
Application logs and events
→ Local collection
→ Redaction and normalisation
→ Shepherd Pie
→ Search, correlation, anomaly detection, dashboards and alerts
```

Secrets, client data and personal information must be redacted before forwarding.

---

## 5. Shared Events and Jobs

All applications should use a common event format.

Examples:

```text
travel.refresh.started
travel.deal.discovered
property.listing.created
green.test.completed
breadcrumbs.build.failed
docker.container.restarted
tg.node.online
backup.completed
crumble.intent.executed
doctor.prescription.applied
deployment.completed
```

Every long-running action must return a job ID and use standard states:

```text
Queued → Running → Waiting → Completed / Failed / Cancelled
```

No request may remain indefinitely at `Thinking`.

Every action must expose:

- loading;
- success;
- timeout;
- error;
- request or job ID;
- supporting logs.

---

## 6. Universal Application Contract

Every managed application should expose:

```text
GET  /health
GET  /manifest
GET  /capabilities
GET  /metrics
GET  /events
GET  /jobs
POST /jobs
GET  /jobs/{job_id}
GET  /settings
POST /settings
```

The manifest should describe the name, family, version, host, icon, dashboard URL, commands, Crumble intents, schedules, permissions, uploads, reports, maps, pipelines and dependencies.

The Control Plane should discover applications from manifests instead of hard-coding every app.

---

## 7. Secure Gateway

Production should expose one secure gateway rather than many public ports.

Suggested routes:

```text
https://jelliedeel/
https://jelliedeel/apps/travelsheep
https://jelliedeel/apps/sealife
https://jelliedeel/apps/geck0earth
https://jelliedeel/apps/greengeck0
https://jelliedeel/apps/breadcrumbs
https://jelliedeel/api/hub
```

The gateway should provide HTTPS, authenticated sessions, role-aware access, service discovery, reverse proxying, request IDs, rate limits, audit events and security headers.

---

## 8. Workspaces and Roles

Required workspaces:

```text
Personal
Ped0na
Professional
Clients
Public Intelligence
Lab
```

Queries, files, jobs, memory and events should belong to a workspace.

Suggested roles:

- Viewer;
- Operator;
- Developer;
- Security Operator;
- Administrator;
- Crumble Agent;
- Remote Device.

Actions should be read-only, routine, privileged or destructive. Privileged and destructive actions require explicit confirmation.

---

## 9. Safe Crumble Execution

Crumble must not translate unrestricted natural language directly into root shell commands.

Required flow:

```text
Input
→ Intent classification
→ Target selection
→ Typed action
→ Permission check
→ Confirmation when required
→ Execution
→ Result
→ Audit event
```

Raw terminal access may exist as a separate mode with stronger authentication and complete auditing.

Crumble memory should initially be suggestive rather than autonomous.

It may learn preferences, repeated searches, dashboard modes, accepted recommendations and common workflows.

It must not autonomously deploy code, delete data, run scans, send communications, make purchases or alter infrastructure.

---

## 10. Build Quality Gates

Every build must pass defined checks before it can be marked deployable.

### Python

- syntax compilation;
- Ruff;
- Black check;
- MyPy;
- Pytest;
- coverage threshold;
- Bandit;
- dependency audit;
- API contract tests;
- migration checks.

### Shell and configuration

- ShellCheck;
- YAML and JSON validation;
- Docker Compose validation;
- schema checks;
- secret scanning.

### Containers

- image build;
- startup;
- health and readiness checks;
- vulnerability scanning;
- licence inventory;
- restart behaviour;
- resource limits.

### Dashboards

- Playwright end-to-end tests;
- every visible button tested;
- authentication and permission tests;
- loading, success, timeout and error states;
- responsive tests;
- accessibility checks;
- screenshots retained as evidence.

### Android

- Gradle build;
- Kotlin lint;
- unit tests;
- Compose UI tests;
- Crumble API integration tests;
- debug APK creation;
- Pixel 8 profile testing;
- generic modern Android compatibility.

Heavy Android and browser testing should run on the Mac or a dedicated runner while JE orchestrates and records results.

---

## 11. Documentation as a Build Output

Every successful build must prepare updates for:

```text
wiki/
release_notes/
change_control/
build_guides/
architecture/
manifests/
deployment_history/
test_reports/
next_steps/
```

Each build report must explain:

- additions;
- changes;
- improvements;
- removals and deprecations;
- database and configuration changes;
- security changes;
- tests and results;
- known limitations;
- rollback instructions;
- unresolved findings;
- future ideas;
- lessons learned.

Generated documentation must be reviewed before final commit and deployment.

---

## 12. Dr Geck0

Dr Geck0 is the scheduled health, quality and improvement service.

Suggested 04:00 weekly schedule:

```text
Monday     Core, JE and Geck0Deploy
Tuesday    TravelSheep and SeaLife
Wednesday  BreadCrumbs and Pink Geck0
Thursday   Green Geck0 and Blue Geck0
Friday     Purple Geck0 and Yellow Geck0
Saturday   Black Geck0 defensive stack
Sunday     Crumble, Home Assistant and Chip Yard
```

TG checks should run only when TG is online and not being used for travel, assignments or authorised testing.

Doctor reports should cover health, APIs, containers, dependencies, databases, disk, resource trends, failed jobs, stale data, security findings, updates, backups, documentation drift, coverage, unusual logs and recommendations.

---

## 13. Doctor Prescriptions

Safe automatic prescriptions may include:

- restarting an unhealthy non-critical container;
- clearing safe temporary caches;
- rotating oversized logs;
- retrying failed scheduled ingestion;
- creating missing non-sensitive directories;
- rebuilding disposable caches;
- approved database maintenance;
- restoring declared service configuration.

Every automatic prescription must:

1. run a dry-run;
2. create a rollback point;
3. use an allowlisted action;
4. write an audit event;
5. verify the outcome;
6. roll back on failure.

Package upgrades, database migrations, firewall changes, authentication changes, deletion, critical rebuilds, connector activation and code deployment require human approval.

---

## 14. Doctor-to-Geck0Deploy Loop

Doctor findings should become structured recommendations with application, severity, category, finding, recommendation, evidence, suggested tests and approval requirement.

Geck0Deploy should combine:

- Doctor findings;
- Shepherd Pie trends;
- failed tests;
- security findings;
- dependency updates;
- user requests;
- Crumble feedback;
- backlog items;
- documentation gaps.

It should produce a proposed build plan for review.

Approval authorises building only. Deployment requires separate approval after tests pass.

---

## 15. Control Plane Modes

### Minimal

- Crumble command bar;
- favourites;
- critical health;
- main app launchers;
- simplified map;
- no raw logs.

### Normal

- service cards;
- schedules;
- jobs;
- application launcher;
- health summaries;
- activity;
- pipelines;
- domain dashboards.

### Maximum

- live logs;
- CPU, memory, disk and temperature;
- Docker events;
- network traffic;
- API requests;
- scheduler events;
- Git activity;
- TG updates;
- Crumble intent traces;
- security alerts;
- graph updates;
- scan progress;
- ingestion counters.

Users should also be able to save custom layouts such as Morning, Travel Planning, Property Hunt, Security Operations, Development, Smart Mirror, Magic Table and Mobile.

---

## 16. Core Vertical Workflows

### TravelSheep and SeaLife

```text
Scheduled refresh
→ connector ingestion
→ normalisation
→ deduplication
→ storage
→ map and list dashboard
→ Crumble query
→ notification
```

### Green Geck0

```text
Submit URL, repository or upload
→ configure test
→ queue job
→ run checks
→ capture evidence
→ generate report
→ deliver or export
```

### BreadCrumbs

```text
Requirements or upload
→ client and project creation
→ repository initialisation
→ planning
→ build
→ Git commit
→ preview
→ Green Geck0 testing
→ security review
→ delivery
```

---

## 17. Home Assistant

Home Assistant is a first-class Registry application.

The Control Plane should support entity discovery, rooms, areas, device health, scenes, automations, sensors, energy, environment, presence, notifications, controlled camera access, service calls and event subscriptions.

Actions must be risk-classified. Reading temperature is read-only; changing a light is routine; unlocking a door or disabling an alarm is privileged.

---

## 18. Chip Yard

Chip Yard manages ESP32 and embedded-device lifecycles.

Responsibilities include:

- device registry;
- board type and capabilities;
- location;
- firmware version;
- OTA updates and rollback;
- heartbeat;
- battery and signal;
- telemetry;
- MQTT discovery;
- per-device credentials;
- provisioning;
- retirement and offline state.

Workflow:

```text
Template
→ firmware configuration
→ build
→ flash or provision
→ enrolment
→ MQTT discovery
→ Home Assistant entity
→ Crumble control
→ Shepherd Pie telemetry
```

Each device should have unique credentials. IoT devices should be isolated on a dedicated network or VLAN where possible.

---

## 19. Notifications and Approvals

The platform needs one inbox for:

- Doctor alerts;
- failed builds;
- security findings;
- backup failures;
- TG state changes;
- deployments;
- travel deals;
- property listings;
- Green Geck0 reports;
- BreadCrumbs reviews;
- Android builds;
- Home Assistant alerts;
- Chip Yard failures.

Delivery should support dashboard, Crumble Android, email, Home Assistant notifications, Telegram or Discord later, and optional voice announcements.

---

## 20. Privacy and Retention

Suggested defaults:

```text
Debug logs           7–14 days
Operational logs     30–90 days
Audit records        long term
Security findings    long term
Raw OSINT             configurable
Client evidence       client-specific
Crumble memory        user-controlled
Home telemetry        sensor-specific
```

Private workspaces must remain isolated from public dashboards and unrelated Crumble queries.

---

## 21. Feature Profiles

Suggested Docker profiles:

```text
core
travel
property
creative
commerce
communications
security
intelligence
home
full
development
```

The Admin dashboard should expose these as controlled toggles.

---

## 22. Observability and Resource Limits

Every service should expose health, readiness, metrics, structured logs, recent errors, job counts and dependency state.

The dashboard should distinguish Healthy, Starting, Degraded, Unhealthy, Stopped and Unknown.

Grafana should provide detailed history. The Control Plane should provide operational summaries and deep links.

Maximum mode should use sampling and rate limits to avoid overloading JE or the browser.

---

## 23. Versioned Migrations and Rollback

Every installer must be safe to rerun.

Before applying a release, Geck0Deploy should:

- detect the installed version;
- validate disk space;
- snapshot configuration;
- back up schemas;
- create a rollback point;
- run migrations;
- start the new release;
- run health checks;
- roll back automatically when critical checks fail.

Each deployment should record version, Git commit, migration version, configuration version, installation time, operator, health result and rollback point.

---

## 24. Disaster Recovery

Backups are not complete until restoration has been tested.

Recovery testing should cover Registry, configuration, PostgreSQL, documentation, Docker services, stable releases, secret references, deployment state and audit history.

Each test should report restored items, duration, missing data, failures and corrective recommendations.

---

## 25. Visual Design

Use a restrained modern hacker aesthetic:

- near-black green-tinted background;
- pale mint primary text;
- brighter green for active states;
- amber for warnings;
- red only for real failures;
- monospace for telemetry;
- modern sans-serif for general text;
- optional grid, noise and scan-line effects;
- consistent icons;
- accessible contrast.

Family accents:

```text
Geck0   green
M0nkey  amber or orange
Li0n    gold
Ped0na  neutral umbrella identity
```

---

## 26. Hard Release Rules

1. Every meaningful action creates an audit event.
2. Every long-running operation has a job ID.
3. Every visible control has loading, success, timeout and error states.
4. Every build passes static analysis, unit, integration and UI tests.
5. Every release generates documentation and rollback metadata.
6. Every Doctor prescription is allowlisted, reversible and audited.
7. No LLM recommendation automatically deploys code.
8. No secrets appear in logs or reports.
9. Home Assistant and Chip Yard use scoped identities.
10. Shepherd Pie receives structured events rather than only raw text.
11. Critical backups have a tested restoration path.
12. Deployment requires explicit human approval after verification.
13. Failed critical health checks block deployment.
14. Every application exposes a manifest, health and capability contract.
15. Every database change uses a versioned migration.
16. Every action is permission checked.
17. External data records provenance and collection time.
18. Offline-node commands have expiry and approval rules.
19. Every release identifies the source Git commit.
20. Every major workflow has an end-to-end automated test.

---

## 27. Implementation Priority

### Must ship next

- audit event model;
- shared job system;
- Shepherd Pie forwarding;
- build quality gates;
- scheduled Doctor inspections;
- Doctor report format;
- safe prescription allowlist;
- approval centre;
- automatic wiki and release documentation;
- Home Assistant integration;
- Chip Yard foundation;
- rollback verification;
- secure gateway;
- application manifests;
- Minimal, Normal and Maximum modes;
- repaired Crumble handling;
- complete TravelSheep and SeaLife workflows;
- complete Green Geck0 flow;
- complete BreadCrumbs flow.

### Should ship

- Android notification and approvals;
- Doctor recommendations dashboard;
- Shepherd Pie correlation views;
- restoration testing;
- workspace retention policies;
- Crumble suggestion explanations;
- Geck0Earth layer tree;
- live firehose;
- saved workspaces;
- Android build trigger;
- Registry, Wiki, Graph and FuseBox screens;
- TG queue visibility.

### Later

- advanced anomaly detection;
- autonomous test environments;
- richer hardware provisioning;
- client self-service;
- public marketplaces;
- advanced SIEM integrations;
- public accounts;
- broader ecommerce;
- complex social integrations.

---

## 28. Core Principle

The platform must remain human-governed.

Automation should reduce repetitive work, collect evidence, surface problems, prepare recommendations, safely perform approved reversible maintenance and help produce tested, documented builds.

Automation must not silently turn recommendations into production changes.

This is the Ped0na governance loop and the shared operational foundation for Geck0, M0nkey, Li0n and every connected application, service and device.

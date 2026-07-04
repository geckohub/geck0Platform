# Black Geck0 Defensive Platform

- **Geck0Trap** — honeypot profile (OpenCanary)
- **Geck0Watch** — IDS/IPS sensor profile (Suricata; capture profile is opt-in)
- **Geck0Sentinel** — lightweight log/SIEM foundation (Loki)
- **Geck0Shield** — future policy, host-hardening and response automation layer

Components are separated and profile-gated so each can later spin out independently. Do not enable packet capture without confirming the correct interface, permissions and storage budget.

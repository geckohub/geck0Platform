# Security defaults

- Local/Tailscale-first; no public exposure by default
- X-Geck0-Token authentication and separate internal scheduler token
- Purple Geck0 encrypts secrets with Fernet
- BreadCrumbs path confinement
- Green Geck0 low-impact checks only
- Packet capture and honeypot profiles disabled until explicitly enabled
- Rotate generated tokens and add TLS/reverse proxy before wider access

- Green Geck0 blocks private, loopback, link-local and reserved targets by default to reduce SSRF risk. Enable `GREEN_ALLOW_PRIVATE=true` only for explicitly authorised lab checks.

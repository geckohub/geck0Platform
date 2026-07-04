# Architecture

JE is the control plane. Domain services expose scoped APIs. Crumble is the human interface. The scheduler triggers TravelSheep Thursday 02:00 and SeaLife daily 11:00 in Europe/London. TG remains an offline-capable worker for GeckoScan/GeckoAir and is intentionally not required for JE services.

The system avoids arbitrary remote shell execution. Crumble dispatches fixed registered intents and service actions. BreadCrumbs is restricted to its managed workspace.

# Validation report

Validated on 4 July 2026 in the build environment.

## Passed

- Python `compileall` across shared modules, services and clients
- YAML parsing for both Compose files and all central configuration files
- Shell syntax checks for installer, rollback, helper scripts and remote clients
- Seven automated pytest checks covering intents, suggestions, service health, BreadCrumbs repo creation, scheduler due logic and Green Geck0 private-target blocking
- FastAPI import/route smoke checks for all eleven services
- Crumble Hub chat, project intent, history, deletion and CORS smoke checks
- Clean installer test in a temporary JE-style directory
- Generated token/password/Fernet key checks
- Rollback snapshot test
- Kotlin delimiter/static structure check for the Android source

## Not executed in this environment

- Docker container build/runtime, because Docker was not available in the build environment. Compose YAML and service imports were validated.
- Android Gradle build/APK generation, because Android SDK 37 and the complete Gradle wrapper runtime were not available. Current source, Gradle versions and wrapper properties are included for Android Studio.
- Live Amadeus/Ticketmaster requests, because credentials were not supplied.

## Expected first-run behaviour

- TravelSheep and SeaLife seed illustrative records immediately.
- Manual/scheduled refreshes enrich TravelSheep from configured connectors.
- Open-Meteo and USGS requests require outbound internet access.
- Production mode requires the generated API token, displayed with `./scripts/show-token.sh`.

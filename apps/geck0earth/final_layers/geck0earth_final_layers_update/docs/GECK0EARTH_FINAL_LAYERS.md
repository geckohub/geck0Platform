# Geck0Earth — Final Layers Update

## 1. Core Base Layers

- OpenStreetMap base map
- Satellite / aerial view
- Terrain / elevation view
- Dark hacker-style map theme
- Minimal dashboard-safe map theme
- Administrative boundaries
- Country / region / council / borough overlays
- Custom Geck0verse location pins

## 2. Environment & Climate Layers

- Weather nowcast
- Rain radar
- Wind speed and direction
- Temperature heat layer
- Flood risk
- River levels
- Coastal erosion / tide zones
- Wildfire risk
- Air quality
- Pollution markers
- Green spaces
- Tree cover
- Rewilding / conservation zones
- SeaLife observation layer

## 3. Crisis / Humanitarian Layers

- Active disasters
- Earthquakes
- Floods
- Fires
- Storms
- Conflict / unrest indicators
- Aid campaign locations
- Verified local organisations
- Donation / campaign links
- Pulse-sourced event summaries
- BreadCrumbs campaign output links

## 4. Travel & Mobility Layers

- UK rail stations
- Train routes
- TravelSheep fare intelligence
- Bus routes
- Ferry routes
- Airports
- Cycle routes
- Walkability zones
- Dog-friendly beaches and parks
- Commute-to-London analysis
- Journey-time heatmaps

## 5. Property / Relocation Layers

- Shared ownership opportunities
- Rental listings
- Dog-friendly property markers
- Coastal towns
- Commute-time overlays
- Affordability bands
- Service charge / rent estimate layer
- Local area notes
- Safety / livability notes
- User shortlist pins

## 6. RF / Signal Intelligence Layers

- Wi-Fi observations from Geck0 Air
- WiGLE imports
- SSID / BSSID heatmaps
- Bluetooth observations
- SDR / Geck0 Radio observations
- FM / AM / CB / aircraft signal markers
- Signal strength radius visualisation
- Historical RF change tracking
- Privacy-safe correlation warnings

## 7. Cyber / Infrastructure Layers

- GeckoScan target geography
- Client asset regions
- Internet-exposed services by location where appropriate
- Cloud exposure notes
- Data centre / hosting region markers
- Public infrastructure status
- Outage indicators
- Blue-team / defensive indicators
- Honeypot / WAF / IDS notes where authorised

## 8. Community / Campaign Layers

- PurpleGeck0 public channels
- Discord / Telegram community markers
- Event locations
- Hacker spaces
- Meetups
- Volunteer opportunities
- RobotRainforest campaign storefront links
- BreadCrumbs-generated campaign sites

## 9. Personal / Private Layers

Private-by-default. Never public unless explicitly exported.

- Ketama walks and favourite places
- Personal travel history
- Photos by location
- Diary / journal location memories
- Home Assistant places
- Trusted device locations
- Private notes and reminders
- Lost-dog alert scan locations

## 10. AI Intelligence / Prediction Layers

- Crumble-generated summaries
- Pulse event detection
- Risk scores
- Trend changes
- Suggested actions
- Recommended campaigns
- Suggested relocation locations
- Suggested dog walks / day trips
- Anomaly detection across sensors and feeds

## Layer Metadata Standard

Every layer should define:

- `id`
- `name`
- `branch`
- `visibility`
- `source_type`
- `update_frequency`
- `privacy_level`
- `requires_api_key`
- `api_key_env`
- `status`
- `notes`

## Ingestion Rule

This update is designed for chronological ZIP ingestion by the Geck0verse updater.

Suggested filename:

`geck0_geck0earth_Final_Layers_Update.zip`

# Geck0 Earth / Geck0 Map

## Vision

Geck0 Earth is a global living atlas combining:

- Encarta-style education
- Google Earth-style exploration
- Google Maps-style local utility
- AI assistant querying
- timeline playback
- real-time data overlays
- personal sensor intelligence
- BreadCrumbs video/documentary generation

It should become the visual intelligence layer of the Geck0 ecosystem.

## Three modes

### 1. Local Mode
Default focus: London / South East England / current user location.

Purpose:
- hyper-local awareness
- commute planning
- shops/restaurants open now
- walking routes
- local air quality
- Wi-Fi/Bluetooth/RF intelligence
- local crime/statistics
- live transport
- events and meetups
- council data
- personal sensor data

Example queries:
- Where is the nearest off-licence still open?
- Can I reach that kebab shop before it closes?
- What is the best green walking route with Ketama?
- What planes are overhead right now?
- What pubs are still open near me?

### 2. UK Mode
Purpose:
- national travel planning
- UK walks and coast paths
- heritage places
- rail/road/ferry/airport connectivity
- census/statistical overlays
- councils/electoral maps
- property, crime, local services

Example layers:
- National Rail
- TfL
- Bus Open Data Service
- National Trust
- Historic England
- National Trails
- UK coast paths
- Environment Agency flood data
- Ordnance Survey boundaries

### 3. Global Mode
Purpose:
- world history
- borders over time
- populations
- wars
- economics
- climate
- disasters
- satellites
- shipping
- flights
- undersea cables
- alternate timelines

Example queries:
- Give me a history of India.
- Show World War II as a 3-minute animation.
- What if dinosaurs had survived?
- Show the COVID pandemic spreading over time.
- Show global undersea telecom cables.

## Core features

### Globe interface
- rotating 3D Earth
- atmospheric layer
- clouds/weather overlays
- fly-to locations
- zoom-aware detail levels

### Timeline engine
- rewind and fast-forward real/historical/speculative events
- playback speeds
- live/past/future mode
- timeline-linked layers

### Layer manager
Every dataset is a toggleable plugin.

Layer categories:
- transport
- environment
- history
- politics
- economy
- local services
- heritage
- nature
- underground
- space
- RF/signal intelligence
- holidays
- alternate timelines

### Story Mode
Natural language prompt creates narrated map sequence.

Example:
"Tell me the history of India"

Output:
- map flight to India
- timeline playback
- narrated script
- border changes
- key events
- photos/videos where available
- export to BreadCrumbs

### Quiz/Game Mode
Interactive learning:
- capitals
- flags
- rivers
- history
- geography
- languages
- astronomy
- transport
- local knowledge

### Holiday Mode
Seasonal overlays:
- Christmas / Santa tracker
- Diwali
- Holi
- Lunar New Year
- Halloween
- Eid
- Hanukkah
- Bonfire Night
- Pride
- Olympics / World Cup

## Data/API catalogue candidates

### Mapping
- OpenStreetMap
- Ordnance Survey APIs
- Natural Earth
- MapLibre / Cesium / deck.gl

### Transport
- TfL Unified API
- National Rail feeds
- Bus Open Data Service
- NaPTAN
- WebTRIS traffic
- OpenSky Network
- ADS-B Exchange / FlightAware where licensed
- AIS vessel APIs
- TfL river services

### Environment
- Met Office
- Environment Agency flood/tide APIs
- UK Hydrographic Office tides
- air quality APIs
- river levels
- water quality

### Space/Astronomy
- NASA imagery
- satellite TLE data
- ISS tracking
- moon phases
- tide/moon relationship
- planet/star positions

### Local intelligence
- WiGLE imports
- Geck0 Air RF data
- Bluetooth scans
- Wi-Fi scans
- SDR data
- ESP32/M5Stack sensors
- Flipper/Pineapple observations
- Cyber Harness logs

### Society/statistics
- ONS census
- UK Police API
- HM Land Registry
- local council data
- planning applications
- electoral boundaries

## MVP build

1. FastAPI backend
2. PostgreSQL/PostGIS database
3. Redis/cache layer
4. MapLibre 2D map first
5. Cesium 3D globe later
6. Plugin layer registry
7. Mock timeline dataset
8. Crumble query endpoint
9. BreadCrumbs export endpoint
10. Wiki docs and manifests

## Next steps

- Build foundation app with sample London layers.
- Add mock transport/weather/history plugins.
- Add local PostGIS tables for observations.
- Add Geck0 Air import format.
- Add Crumble query endpoint.
- Add BreadCrumbs story export JSON.

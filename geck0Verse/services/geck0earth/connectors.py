from shared.http import fetch_json
async def weather(lat,lon):return await fetch_json("https://api.open-meteo.com/v1/forecast",params={"latitude":lat,"longitude":lon,"current":"temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m","timezone":"auto"})
async def air_quality(lat,lon):return await fetch_json("https://air-quality-api.open-meteo.com/v1/air-quality",params={"latitude":lat,"longitude":lon,"current":"pm10,pm2_5,carbon_monoxide,nitrogen_dioxide,ozone,european_aqi","timezone":"auto"})
async def marine(lat,lon):return await fetch_json("https://marine-api.open-meteo.com/v1/marine",params={"latitude":lat,"longitude":lon,"current":"wave_height,wave_direction,wave_period,sea_surface_temperature","timezone":"auto"})
async def earthquakes():
    data=await fetch_json("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson")
    return [{"id":f.get('id'),"lat":f['geometry']['coordinates'][1],"lon":f['geometry']['coordinates'][0],"magnitude":f['properties'].get('mag'),"place":f['properties'].get('place')} for f in data.get('features',[])[:250]]

async def geocode(query):
    return await fetch_json("https://geocoding-api.open-meteo.com/v1/search",params={"name":query,"count":10,"language":"en","format":"json"})

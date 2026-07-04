from datetime import date,timedelta
import os,asyncio
from shared.http import fetch_json
DESTINATIONS=[("Brighton",50.8225,-0.1372,78),("Hastings",50.8552,0.5729,68),("Margate",51.3813,1.3862,72),("Bath",51.3811,-2.3590,112),("York",53.9599,-1.0873,146),("Bristol",51.4545,-2.5879,108)]
async def sample_deals():
    friday=date.today()+timedelta((4-date.today().weekday())%7+7); deals=[]
    for idx,(city,lat,lon,base) in enumerate(DESTINATIONS):
        travel=base+(idx%3)*9;stay=58+(idx%4)*13
        deals.append({"id":f"sample-{city.lower()}","destination":city,"lat":lat,"lon":lon,"depart":friday.isoformat(),"return":(friday+timedelta(days=2)).isoformat(),"travel_price":travel,"stay_price":stay,"total_price":travel+stay,"currency":"GBP","source":"sample","summary":f"Weekend suggestion for {city}","url":None})
    return deals
async def enrich_weather(deals):
    async def one(d):
        try:
            data=await fetch_json("https://api.open-meteo.com/v1/forecast",params={"latitude":d["lat"],"longitude":d["lon"],"daily":"temperature_2m_max,precipitation_probability_max","forecast_days":7,"timezone":"Europe/London"},timeout=6.0)
            daily=data.get("daily",{});d["weather"]={"max_c":(daily.get("temperature_2m_max") or [None])[-1],"rain_probability":(daily.get("precipitation_probability_max") or [None])[-1]}
        except Exception:d["weather"]={"status":"unavailable"}
        return d
    return list(await asyncio.gather(*(one(d) for d in deals)))
async def generic_json_feed():
    url=os.getenv("TRAVELSHEEP_JSON_FEED_URL","").strip()
    if not url:return []
    data=await fetch_json(url);return data.get("deals",data if isinstance(data,list) else [])
async def ticketmaster_events(city):
    key=os.getenv("TICKETMASTER_API_KEY","").strip()
    if not key:return []
    data=await fetch_json("https://app.ticketmaster.com/discovery/v2/events.json",params={"apikey":key,"city":city,"countryCode":"GB","size":5})
    return [{"name":e.get("name"),"url":e.get("url"),"date":e.get("dates",{}).get("start",{}).get("localDate")} for e in data.get("_embedded",{}).get("events",[])]

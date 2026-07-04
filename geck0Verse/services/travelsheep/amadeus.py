import os
import httpx

BASE=os.getenv("AMADEUS_BASE_URL","https://test.api.amadeus.com")
async def token():
    client=os.getenv("AMADEUS_CLIENT_ID","").strip(); secret=os.getenv("AMADEUS_CLIENT_SECRET","").strip()
    if not client or not secret: raise RuntimeError("Amadeus credentials are not configured")
    async with httpx.AsyncClient(timeout=20) as h:
        r=await h.post(f"{BASE}/v1/security/oauth2/token",data={"grant_type":"client_credentials","client_id":client,"client_secret":secret})
        r.raise_for_status(); return r.json()["access_token"]
async def flight_offers(origin,destination,departure_date,return_date=None,adults=1,max_price=200):
    access=await token(); params={"originLocationCode":origin.upper(),"destinationLocationCode":destination.upper(),"departureDate":departure_date,"adults":adults,"currencyCode":"GBP","maxPrice":max_price,"max":20}
    if return_date: params["returnDate"]=return_date
    async with httpx.AsyncClient(timeout=30) as h:
        r=await h.get(f"{BASE}/v2/shopping/flight-offers",params=params,headers={"Authorization":f"Bearer {access}"})
        r.raise_for_status(); return r.json()

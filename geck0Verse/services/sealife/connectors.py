import csv,os
from pathlib import Path
from shared.http import fetch_json
SAMPLE=[
{"id":"demo-bri-1","town":"Brighton","lat":50.8278,"lon":-0.1527,"bedrooms":2,"tenure":"rent","price":1650,"period":"pcm","title":"Two-bedroom flat near Preston Park","source":"sample","url":None},
{"id":"demo-bri-2","town":"Brighton","lat":50.8195,"lon":-0.1363,"bedrooms":2,"tenure":"shared_ownership","price":122500,"share_percent":40,"title":"Two-bedroom shared ownership apartment","source":"sample","url":None},
{"id":"demo-has-1","town":"Hastings","lat":50.8555,"lon":0.5760,"bedrooms":2,"tenure":"rent","price":1150,"period":"pcm","title":"Two-bedroom St Leonards rental","source":"sample","url":None},
{"id":"demo-has-2","town":"Hastings","lat":50.8580,"lon":0.5850,"bedrooms":2,"tenure":"ownership","price":235000,"title":"Two-bedroom coastal flat","source":"sample","url":None},
{"id":"demo-mar-1","town":"Margate","lat":51.3850,"lon":1.3860,"bedrooms":2,"tenure":"rent","price":1100,"period":"pcm","title":"Two-bedroom Cliftonville rental","source":"sample","url":None},
{"id":"demo-mar-2","town":"Margate","lat":51.3810,"lon":1.3760,"bedrooms":2,"tenure":"shared_ownership","price":98000,"share_percent":35,"title":"Two-bedroom shared ownership home","source":"sample","url":None}]
async def load_all():
    items=list(SAMPLE);url=os.getenv("SEALIFE_JSON_FEED_URL","").strip()
    if url:
        data=await fetch_json(url);items.extend(data.get("listings",data if isinstance(data,list) else []))
    csv_path=Path(os.getenv("SEALIFE_CSV_PATH","/data/sealife/import/listings.csv"))
    if csv_path.exists():
        with csv_path.open(newline='',encoding='utf-8') as f:items.extend(dict(r) for r in csv.DictReader(f))
    return items

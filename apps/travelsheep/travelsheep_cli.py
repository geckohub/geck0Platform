import sys, json, pathlib, datetime
root=pathlib.Path.home()/'geck0Platform/apps/travelsheep'; data=root/'data'; data.mkdir(parents=True,exist_ok=True)
cmd=sys.argv[1:] or ['deals']
seed=[{'name':'Dog-friendly cottage demo','area':'Brighton/Hastings/Margate radius','price_per_night':95,'dog_friendly':True,'lat':50.85,'lon':0.58,'source':'placeholder scraper'}]
(data/'deals.json').write_text(json.dumps({'updated':datetime.datetime.utcnow().isoformat(),'items':seed},indent=2))
(data/'osm_overlay.geojson').write_text(json.dumps({'type':'FeatureCollection','features':[{'type':'Feature','geometry':{'type':'Point','coordinates':[x['lon'],x['lat']]},'properties':x} for x in seed]},indent=2))
print('🐑 TravelSheep ready. Wrote deals.json and osm_overlay.geojson. Next: connect cottage/booking APIs or approved scrapers.')

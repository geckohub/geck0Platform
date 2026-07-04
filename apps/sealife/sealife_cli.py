import sys,json,pathlib,datetime
root=pathlib.Path.home()/'geck0Platform/apps/sealife'; data=root/'data'; data.mkdir(parents=True,exist_ok=True)
homes=[{'title':'Shared ownership demo flat','town':'Brighton','beds':1,'price':'TBC','lat':50.8225,'lon':-0.1372,'source':'placeholder scraper'}]
(data/'homes.json').write_text(json.dumps({'updated':datetime.datetime.utcnow().isoformat(),'items':homes},indent=2))
(data/'osm_overlay.geojson').write_text(json.dumps({'type':'FeatureCollection','features':[{'type':'Feature','geometry':{'type':'Point','coordinates':[x['lon'],x['lat']]},'properties':x} for x in homes]},indent=2))
print('🌊 SeaLife ready. Wrote homes.json and osm_overlay.geojson. Next: connect shared ownership sources.')

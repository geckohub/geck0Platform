#!/usr/bin/env python3
import sys,json,datetime,os
root=os.path.expanduser('~/geck0Platform/apps/shopbot')
os.makedirs(root+'/data',exist_ok=True)
cmd=sys.argv[1] if len(sys.argv)>1 else 'status'
q=' '.join(sys.argv[2:]) if len(sys.argv)>2 else 'electronics deals'
items=[{'query':q,'title':'Example electronics deal placeholder','price':'TBC','source':'configure SHOPBOT_SEARCH_API_KEY or scraper adapter','ts':datetime.datetime.now(datetime.UTC).isoformat()}]
open(root+'/data/latest_deals.json','w').write(json.dumps(items,indent=2))
print('ShopBot wrote',root+'/data/latest_deals.json')

#!/usr/bin/env python3
import os
HOME=os.path.expanduser('~')
env=os.path.join(HOME,'geck0Platform','config','.env')
keys=['OPENAI_API_KEY','ANTHROPIC_API_KEY','GEMINI_API_KEY','GROK_API_KEY','TFL_APP_KEY','OPENWEATHER_API_KEY','DISCORD_WEBHOOK_URL','TELEGRAM_BOT_TOKEN','LINODE_TOKEN','SHOPBOT_SEARCH_API_KEY']
vals={}
if os.path.exists(env):
    for line in open(env):
        if '=' in line and not line.strip().startswith('#'):
            k,v=line.strip().split('=',1); vals[k]=v
print('🔌 Integration readiness')
for k in keys:
    print(('✅' if vals.get(k) else '⚠️'), k, 'configured' if vals.get(k) else 'missing')

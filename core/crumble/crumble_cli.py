import sys, os, sqlite3, pathlib, datetime, json
root=pathlib.Path(os.environ.get('GECK0_ROOT', pathlib.Path.home()/'geck0Platform'))
text=' '.join(sys.argv[1:]).strip() or 'status'
con=sqlite3.connect(root/'knowledge/geck0_knowledge.db')
persona=os.environ.get('CRUMBLE_PERSONA','wise_friend')
# fast local intent scaffold
if 'status' in text.lower() or 'doctor' in text.lower():
    response='Crumble: local platform status available via geck0 doctor. Registry, knowledge DB and app scaffolds are installed.'
elif 'backup' in text.lower():
    response='Crumble: run geck0 backup to create a timestamped archive and optional Linode sync.'
elif 'travel' in text.lower():
    response='Crumble: routing to TravelSheep. Try travelsheep refresh or travelsheep deals.'
elif 'sea' in text.lower() or 'flat' in text.lower():
    response='Crumble: routing to SeaLife. Try sealife refresh or sealife homes.'
else:
    response=f'Crumble [{persona}]: I heard: {text}. Cloud/Ollama adapters are scaffolded; connect API keys in ~/geck0Platform/config/.env.'
con.execute('insert into commands(ts,persona,text,response) values (?,?,?,?)',(datetime.datetime.utcnow().isoformat(),persona,text,response)); con.commit()
print(response)

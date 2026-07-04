from collections import Counter
from .registry import load_yaml
def classify(text:str)->dict:
    normalized=text.casefold().strip(); best={"name":"general_chat","score":0.0,"action":None}
    for item in load_yaml("intents.yaml").get("intents",[]):
        hits=sum(1 for p in item.get("patterns",[]) if p.casefold() in normalized)
        if hits:
            score=min(1.0,hits/max(1,len(item.get("patterns",[])))+0.45)
            if score>best["score"]: best={"name":item["name"],"score":score,"action":item.get("action")}
    return best
def suggestions(history:list[str],limit:int=5)->list[str]:
    ranked=[x for x,_ in Counter(h.strip().casefold() for h in history if h.strip()).most_common(limit)]
    for d in ["Show the latest TravelSheep deals","Show new SeaLife listings","Show Geck0Earth layers","Show project status"]:
        if d.casefold() not in ranked and len(ranked)<limit: ranked.append(d)
    return ranked[:limit]

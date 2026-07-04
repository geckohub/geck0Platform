from shared.intents import classify,suggestions
def test_travel_intent():assert classify("show me travel deals")["name"]=="travelsheep_latest"
def test_suggestions():assert len(suggestions(["travel deals","travel deals"]))>=1

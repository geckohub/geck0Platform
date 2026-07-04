from fastapi.testclient import TestClient
from services.hub.app import app as hub
from services.travelsheep.app import app as travel
from services.sealife.app import app as sea
def test_health():
 assert TestClient(hub).get('/health').status_code==200
 assert TestClient(travel).get('/health').status_code==200
 assert TestClient(sea).get('/health').status_code==200

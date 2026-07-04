import requests

class CrumbleClient:
    def __init__(self, base_url="http://localhost:8890"):
        self.base_url = base_url.rstrip("/")

    def status(self):
        return requests.get(f"{self.base_url}/status", timeout=3).json()

    def command(self, text: str):
        return requests.post(f"{self.base_url}/command", json={"text": text}, timeout=5).json()

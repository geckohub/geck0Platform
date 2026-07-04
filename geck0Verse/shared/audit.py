from datetime import datetime, timezone
import json
from .settings import settings
def audit(service: str, action: str, details: dict | None = None) -> None:
    path = settings.data_root / "audit" / f"{service}.jsonl"; path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f: f.write(json.dumps({"ts":datetime.now(timezone.utc).isoformat(),"service":service,"action":action,"details":details or {}},ensure_ascii=False)+"\n")

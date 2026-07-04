from __future__ import annotations
import os
from dataclasses import dataclass
from pathlib import Path
@dataclass(frozen=True)
class Settings:
    env: str = os.getenv("GECK0_ENV", "development")
    api_token: str = os.getenv("GECK0_API_TOKEN", "dev-token")
    internal_token: str = os.getenv("GECK0_INTERNAL_TOKEN", "internal-dev-token")
    data_root: Path = Path(os.getenv("GECK0_DATA_ROOT", "/tmp/geck0verse-data"))
    timezone: str = os.getenv("GECK0_TIMEZONE", "Europe/London")
    database_url: str = os.getenv("DATABASE_URL", "sqlite:////tmp/geck0verse.db")
    dev_mode: bool = os.getenv("GECK0_ENV", "development") == "development"
settings = Settings()
settings.data_root.mkdir(parents=True, exist_ok=True)

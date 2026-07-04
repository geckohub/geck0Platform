from fastapi import Header, HTTPException, status
from .settings import settings
def require_token(x_geck0_token: str | None = Header(default=None)) -> str:
    if settings.dev_mode and not x_geck0_token: return "development"
    if x_geck0_token not in {settings.api_token, settings.internal_token}:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Geck0 token")
    return x_geck0_token or ""

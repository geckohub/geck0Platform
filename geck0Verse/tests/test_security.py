import pytest
from services.greengeck0.runner import guard_host
def test_private_target_blocked(monkeypatch):
 monkeypatch.delenv("GREEN_ALLOW_PRIVATE",raising=False)
 with pytest.raises(ValueError):guard_host("127.0.0.1")

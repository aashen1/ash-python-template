"""Shared test fixtures."""

from __future__ import annotations

import pytest

# All env vars that Settings reads; clearing them ensures each test
# starts from the declared defaults rather than inheriting the host
# environment.
_SETTINGS_ENV_KEYS = [
    "APP_NAME",
    "APP_ENV",
    "APP_DEBUG",
    "APP_VERSION",
    "LOG_LEVEL",
    "LOG_JSON",
]


@pytest.fixture(autouse=True)
def _isolate_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    """Ensure every test starts with default Settings values."""
    for key in _SETTINGS_ENV_KEYS:
        monkeypatch.delenv(key, raising=False)
    from change_to_your_name.config import get_settings

    get_settings.cache_clear()

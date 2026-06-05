"""Tests for the typed :class:`Settings` configuration class."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from change_to_your_name.config import Settings, get_settings


def test_default_settings() -> None:
    """Defaults match the values declared in the Settings class."""
    settings = Settings(_env_file=None)
    assert settings.app_name == "change-to-your-name"
    assert settings.app_env == "development"
    assert settings.app_debug is True
    assert settings.log_level == "INFO"
    assert settings.log_json is False
    assert settings.api_timeout_seconds == 30
    assert settings.api_max_retries == 3


def test_environment_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Environment variables override the default values."""
    monkeypatch.setenv("APP_NAME", "from-env")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("LOG_JSON", "true")
    monkeypatch.setenv("API_TIMEOUT_SECONDS", "5")

    settings = Settings(_env_file=None)

    assert settings.app_name == "from-env"
    assert settings.log_level == "DEBUG"
    assert settings.log_json is True
    assert settings.api_timeout_seconds == 5


def test_invalid_log_level_rejected() -> None:
    """An unknown log level is rejected by pydantic validation."""
    with pytest.raises(ValidationError):
        Settings(log_level="NOTALEVEL", _env_file=None)  # type: ignore[arg-type]


def test_invalid_app_env_rejected() -> None:
    """An unknown app environment is rejected by pydantic validation."""
    with pytest.raises(ValidationError):
        Settings(app_env="prod", _env_file=None)  # type: ignore[arg-type]


def test_api_timeout_bounds() -> None:
    """The ``api_timeout_seconds`` field enforces its declared bounds."""
    with pytest.raises(ValidationError):
        Settings(api_timeout_seconds=0, _env_file=None)


def test_get_settings_cached(monkeypatch: pytest.MonkeyPatch) -> None:
    """``get_settings`` returns the same instance on repeated calls."""
    monkeypatch.setenv("APP_NAME", "cached")
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
    assert first.app_name == "cached"
    get_settings.cache_clear()

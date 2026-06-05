"""Tests for the typed :class:`Settings` configuration class."""

from __future__ import annotations

import pytest
from pydantic import ValidationError

from change_to_your_name.config import Settings, get_settings


def test_default_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    """Defaults match the values declared in the Settings class."""
    # Clear any env vars that might override defaults
    for key in ["APP_NAME", "APP_ENV", "APP_DEBUG", "LOG_LEVEL", "LOG_JSON"]:
        monkeypatch.delenv(key, raising=False)
    settings = Settings()
    assert settings.app_name == "change-to-your-name"
    assert settings.app_env == "development"
    assert settings.app_debug is True
    assert settings.log_level == "INFO"
    assert settings.log_json is False


def test_environment_override(monkeypatch: pytest.MonkeyPatch) -> None:
    """Environment variables override the default values."""
    monkeypatch.setenv("APP_NAME", "from-env")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")
    monkeypatch.setenv("LOG_JSON", "true")

    settings = Settings()

    assert settings.app_name == "from-env"
    assert settings.log_level == "DEBUG"
    assert settings.log_json is True


def test_invalid_log_level_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    """An unknown log level is rejected by pydantic validation."""
    monkeypatch.delenv("LOG_LEVEL", raising=False)
    with pytest.raises(ValidationError):
        Settings(log_level="NOTALEVEL")  # type: ignore[arg-type]


def test_invalid_app_env_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    """An unknown app environment is rejected by pydantic validation."""
    monkeypatch.delenv("APP_ENV", raising=False)
    with pytest.raises(ValidationError):
        Settings(app_env="prod")  # type: ignore[arg-type]


def test_get_settings_cached(monkeypatch: pytest.MonkeyPatch) -> None:
    """``get_settings`` returns the same instance on repeated calls."""
    monkeypatch.setenv("APP_NAME", "cached")
    get_settings.cache_clear()
    first = get_settings()
    second = get_settings()
    assert first is second
    assert first.app_name == "cached"
    get_settings.cache_clear()

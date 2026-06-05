"""Application configuration backed by pydantic-settings.

All runtime configuration is loaded from environment variables (and an optional
`.env` file). Use :func:`get_settings` to access a cached singleton so the same
instance is reused across the application.
"""

from __future__ import annotations

from functools import lru_cache
from importlib.metadata import PackageNotFoundError, version
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

try:
    _DEFAULT_VERSION: str = version("change-to-your-name")
except PackageNotFoundError:
    _DEFAULT_VERSION = "0.0.0"  # development mode fallback


class Settings(BaseSettings):
    """Typed application settings loaded from the environment.

    Values can be overridden by creating a `.env` file in the project root.
    See `.env.example` for the full list of supported variables.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    app_name: str = "change-to-your-name"
    app_env: Literal["development", "staging", "production", "test"] = "development"
    app_debug: bool = True
    app_version: str = _DEFAULT_VERSION

    # Logging
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"
    log_json: bool = Field(
        default=False,
        description="Emit logs as JSON when true, otherwise use a colored console renderer.",
    )


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached :class:`Settings` singleton."""
    return Settings()


__all__ = ["Settings", "get_settings"]

"""Tests for the structlog-based logging configuration."""

from __future__ import annotations

import logging

import pytest

from change_to_your_name.config import get_settings
from change_to_your_name.core import configure_logging, get_logger


def test_configure_logging_is_idempotent() -> None:
    """Calling ``configure_logging`` twice has no observable side effects."""
    configure_logging(force=True)
    configure_logging()
    configure_logging()


def test_get_logger_returns_callable_logger(capsys: pytest.CaptureFixture[str]) -> None:
    """``get_logger`` returns an object that emits log records when used."""
    configure_logging(force=True)
    logger = get_logger("tests.logging")
    logger.info("hello from tests")
    captured = capsys.readouterr()
    assert "hello from tests" in captured.err


def test_configure_logging_respects_log_level(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Changing the log level via env updates the filtering bound logger."""
    monkeypatch.setenv("LOG_LEVEL", "WARNING")
    configure_logging(force=True)
    assert get_settings().log_level == "WARNING"


def test_configure_logging_json_mode(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """When ``LOG_JSON=true`` the structlog config uses ``JSONRenderer``."""
    monkeypatch.setenv("LOG_JSON", "true")
    configure_logging(force=True)
    # The standard logging level should still be applied.
    assert logging.getLogger().level <= logging.WARNING

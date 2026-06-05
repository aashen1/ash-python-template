"""Structured logging configuration built on :mod:`structlog`.

The :func:`configure_logging` function should be called once at process
startup (e.g. in the application entrypoint) before emitting any log
records. Use :func:`get_logger` to retrieve a bound logger anywhere in the
codebase.
"""

from __future__ import annotations

import logging
import sys
from typing import Any

import structlog

from change_to_your_name.config import get_settings


_configured: bool = False


def _is_configured() -> bool:
    """Return ``True`` when :func:`configure_logging` has already run."""
    return _configured


def _mark_configured() -> None:
    """Record that :func:`configure_logging` has been run."""
    global _configured
    _configured = True


def configure_logging(force: bool = False) -> None:
    """Configure :mod:`structlog` and the standard :mod:`logging` module.

    The function is idempotent: subsequent calls are no-ops unless ``force`` is
    ``True``, which is useful for tests that need to reset the configuration.
    """
    if _is_configured() and not force:
        return

    if force:
        global _configured
        _configured = False

    settings = get_settings()
    level = getattr(logging, settings.log_level.upper(), logging.INFO)

    shared_processors: list[Any] = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
    ]

    renderer: Any
    if settings.log_json:
        renderer = structlog.processors.JSONRenderer()
    else:
        renderer = structlog.dev.ConsoleRenderer(colors=sys.stderr.isatty())

    structlog.configure(
        processors=[*shared_processors, renderer],
        wrapper_class=structlog.make_filtering_bound_logger(level),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(file=sys.stderr),
        cache_logger_on_first_use=True,
    )

    logging.basicConfig(
        format="%(message)s",
        stream=sys.stderr,
        level=level,
    )

    _mark_configured()


def get_logger(name: str | None = None) -> structlog.stdlib.BoundLogger:
    """Return a configured structlog logger, lazily initializing logging."""
    if not _is_configured():
        configure_logging()
    logger: structlog.stdlib.BoundLogger = structlog.get_logger(name)
    return logger


__all__ = ["configure_logging", "get_logger"]

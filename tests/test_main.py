"""Smoke tests for the ``__main__`` entrypoint using ``pytest-mock``."""

from __future__ import annotations

import pytest

from change_to_your_name import __main__ as entry
from change_to_your_name import __version__
from change_to_your_name.__main__ import main


def test_main_emits_startup_log(mocker: pytest.MockerFixture) -> None:
    """``main()`` configures logging and emits a structured startup log."""
    configure_spy = mocker.patch.object(entry, "configure_logging")
    logger_spy = mocker.patch.object(entry, "get_logger")

    main()

    configure_spy.assert_called_once_with()
    logger_spy.assert_called_once_with("change_to_your_name.__main__")
    bound = logger_spy.return_value
    bound.info.assert_called_once_with(
        "starting", app="change-to-your-name", version=__version__
    )


def test_main_uses_logging_helper() -> None:
    """The main module exposes ``main``, ``configure_logging`` and ``get_logger``."""
    assert callable(entry.main)
    assert hasattr(entry, "configure_logging")
    assert hasattr(entry, "get_logger")

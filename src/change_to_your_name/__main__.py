"""Command-line entry point for the change-to-your-name package.

Run with ``python -m change_to_your_name``.
"""

from __future__ import annotations

from change_to_your_name import __version__
from change_to_your_name.core import configure_logging, get_logger


def main() -> None:
    """Entry point: configure logging and emit a startup banner."""
    configure_logging()
    logger = get_logger(__name__)
    logger.info("starting", app="change-to-your-name", version=__version__)


if __name__ == "__main__":
    main()

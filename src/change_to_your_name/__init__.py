"""Change-to-your-name: A Python project."""

from importlib.metadata import PackageNotFoundError, version

from change_to_your_name.config import Settings, get_settings

try:
    __version__ = version("change-to-your-name")
except PackageNotFoundError:
    __version__ = "0.0.0"  # development mode fallback

__all__ = ["Settings", "__version__", "get_settings"]

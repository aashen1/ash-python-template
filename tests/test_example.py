from change_to_your_name import Settings, __version__, get_settings


def test_version() -> None:
    assert isinstance(__version__, str) and len(__version__) > 0


def test_public_api_exports() -> None:
    """The package exposes ``Settings``, ``__version__`` and ``get_settings``."""
    assert Settings is not None
    assert callable(get_settings)

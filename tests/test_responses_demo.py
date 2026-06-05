"""Example test that uses the ``responses`` library to mock HTTP calls.

This is a template for tests that need to stub external HTTP services
without performing real network requests. The function exercised here
is intentionally trivial; it is meant to demonstrate the mocking
pattern rather than provide production code.
"""

from __future__ import annotations

import requests
import responses

from change_to_your_name.config import Settings


@responses.activate
def test_responses_mocks_http_call() -> None:
    """``responses`` can stub HTTP calls and the stub is hit by the request."""
    settings = Settings(_env_file=None)
    url = "https://example.com/api"

    responses.add(
        method=responses.GET,
        url=url,
        json={"app": settings.app_name},
        status=200,
    )

    response = requests.get(url, timeout=5)

    assert response.status_code == 200
    assert response.json() == {"app": settings.app_name}
    assert len(responses.calls) == 1
    assert responses.calls[0].request.url == url

import pytest
from starlette.testclient import TestClient

from smilestoimg.app import app


@pytest.yield_fixture
def rest_client() -> TestClient:
    """Returns a FastAPI test client."""

    with TestClient(app) as client:
        yield client

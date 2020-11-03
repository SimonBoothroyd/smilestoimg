from smilestoimg.core.config import settings


def test_smiles_endpoint(rest_client):
    """Sample test, will always pass so long as import statement worked"""
    svg_request = rest_client.get(
        "http://testserver/api/dev/smiles/CO",
        headers={"access_token": settings.ACCESS_TOKEN},
    )
    svg_request.raise_for_status()
    assert "</svg>" in svg_request.text

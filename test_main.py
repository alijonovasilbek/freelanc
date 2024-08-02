import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from main import app  # FastAPI dasturingizning asosiy fayli
from httpx import ASGITransport

@pytest.mark.asyncio
async def test_get_public_gigs():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        response = await client.get("/gigss")
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    if data:
        assert "id" in data[0]
        assert "gigs_title" in data[0]
        assert "price" in data[0]


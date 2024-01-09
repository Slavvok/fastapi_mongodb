import pytest
from fastapi.testclient import TestClient
from pydantic import BaseModel

from app import app
from routes.auth import get_current_user

client = TestClient(app)


class UserMock(BaseModel):
    id: str


@pytest.fixture(autouse=True)
def mock_no_authentication():
    app.dependency_overrides[get_current_user] = lambda: UserMock(
        id="user_id"
    )


def test_get_number_success(monkeypatch):
    # monkeypatch.setattr("connector.client", AsyncMongoMockClient())
    number = 1
    #    async with AsyncClient(app=app, base_url=f"http://{BASE_URL}/numbers") as ac:
#         response = await ac.get("/")
#     token = client.post("/token/", data={"username": USERNAME, "password": PASSWORD})
#     token = token.json()["access_token"]
#     headers = {"Authorization": f"Bearer {token}", "accept": "application/json"}
    response = client.get('/number/', params={"number": number})
    assert response.json() == {"number": 1}

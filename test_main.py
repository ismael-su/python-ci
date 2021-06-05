from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


def test_get_devs():
    response = client.get("/users/dev")
    assert response.status_code == 200
    assert response.json() == {"data": ['Joris', 'Ismael', 'Lucas']}

from app import app

def test_home():  # ✅ must start with test_
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
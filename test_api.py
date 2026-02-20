import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data
def test_create_user():
    payload = {"name": "morpheus", "username": "morpheus", "email": "morpheus@example.com"}
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "morpheus"
    assert data["username"] == "morpheus"
def test_update_user():
    payload = {"name": "morpheus", "username": "zionresident", "email": "zion@example.com"}
    response = requests.put("https://jsonplaceholder.typicode.com/users/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "zionresident"
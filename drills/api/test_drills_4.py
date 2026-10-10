import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Drill 1: Test that creating a user with POST returns status 201 (created).

def test_create_user_returns_201():
    response = requests.post(f"{BASE_URL}/users", json={"name": "SAM"})
    assert response.status_code == 201

# Drill 2: Test that the users list endpoint returns a non-empty list.

def test_users_list_not_empty():
    response = requests.get(f"{BASE_URL}/users")

    data = response.json()
    assert len(data) > 0
    

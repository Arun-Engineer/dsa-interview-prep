def test_get_user(playwright):
    api = playwright.request.new_context(base_url = "https://jsonplaceholder.typicode/com")

    response = api.get("/users/1")

    assert response.status == 200

    data = response.json()

    assert data["id"] == 1

    api.dispose()

def test_create_post(playwright):
    api = playwright.request.new_context(base_url = "https://jsonplaceholder.typicode.com")

    response = api.post("/posts", data = {"title": "test", "body": "hello"})

    assert response.status == 201
    api.dispose()
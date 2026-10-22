def test_api_with_playwright(playwright):
    request_context = playwright.request.new_context()
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status == 200
    data = response.json()
    assert data["id"] == 1
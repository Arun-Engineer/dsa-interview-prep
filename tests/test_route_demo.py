def fake_page(route):

    route.fulfill(
        status = 200,
        content_type = "text/html",
        body = "<h1> Out Of Stock </h1>"
    )


def test_fake_out_of_stock_page(page):
    page.route("https://example.com", fake_page)

    page.goto("https://example.com")

    heading = page.locator("h1").inner_text()
    print("Heading on screen:", heading)
    assert heading == "Out Of Stock"
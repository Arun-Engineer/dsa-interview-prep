# saucedemo has a sort dropdown ("Name A-Z", "Price low-high")
page.locator(".product_sort_container").select_option("lohi") # by vlaue
page.get_by_role("combobox").select_option(lable = "Price (low to high)") # by visible text
page.getlocator(".product_sort_container").select_option(index = 2) # by index

# press() keyboard keys asks  you asked for this specifically

# simulates pressing a key

page.get_by_placeholder("Search").press("Enter") # press ENter to submit
page.get_by_placeholder("Username").press("Tab") # Tab to next field
page.press("body", "Control+A") 

# type() vs  fill()
page.get_by_placeholder("Search").fill("shoes")
page.get_by_placeholder("search").press_sequentially("shoes", delay = 100)

# check vs uncheck
page.get_by_label("Remember me").check() # tick it
page.get_by_label("Subscrible").uncheck() # untick it
expect(page.get_by_label("Remember me")).to_be_checked() # assert state

# hover()
page.get_by_role("menuitem", name = "Products").hover() 

# Explicit waits(for custom conditions playwright cant guess)

# wait_for_specific_url
page.wait_for_url("**/inventory.html")

# wait for the newtork to go quiet(all requests done)
page.wait_for_load_state("newtorkidle")

# wait for a specific element to reach a state
page.get_by_text("Loaded").wait_for(state = "visible")

# wait for an element to appear in the DOM
page.wait_for_selector(".inventory_list")

# wait for custom .Js notifications
page.wait_for_function("() => document.title === Done")

def test_login():
    # 1. Go to page and wait for it to load:
    page.goto("https://www.saucedemo.com")
    page.wait_for_laod_state("networkidle")

    # 2. wait for login form to appear:
    page.wait_for_selector(".login-box")

    # 3. Fill in credentials
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # 4. Wait for redirect to inventory
    page.wait_for_url("**/inventory.html")

    # 5. Wait for products to appear
    page.get_by_text("Products").wait_for(state = "visible")

    # 6. wait for all products to load.
    page.wait_for_function("() => document.title === Done")
    # or
    page.wait_for_function("() => document.querySelectorAll('.inventory_item'). length > 0")

    print("Login Test Passed.")
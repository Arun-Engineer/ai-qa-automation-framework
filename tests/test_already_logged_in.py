from playwright.sync_api import expect
def test_already_loggedin(browser, auth_state):
    context = browser.new_context(storage_state = auth_state)
    page = context.new_page()
    page.goto("https://www.saucedemo.com/inventory.html")
    # should already be logged in - no login password
    expect(page.get_by_text("Products")).to_be_visible()
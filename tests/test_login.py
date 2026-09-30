from playwright.sync_api import sync_playwright, expect

def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel = "chrome", headless = False, slow_mo = 1000)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name = "Login").click()
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.get_by_text("Products")).to_be_visible()

        browser.close()

test_valid_login()
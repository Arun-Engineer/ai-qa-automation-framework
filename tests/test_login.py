from playwright.sync_api import Page, sync_playwright, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# def test_valid_login():
#     with sync_playwright() as p:
#         browser = p.launch(channel = "chrome", headless = False, slow_mo = 1000)
#         page = browser.new_page()
#         page.goto("https://www.saucedemo.com/")

#         page.get_by_placeholder("Username").fill("standard_user")
#         page.get_by_placeholder("Password").fill("secret_sauce")
#         page.get_by_role("button", name = "Login").click()
#         expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
#         expect(page.get_by_text("Products")).to_be_visible()

#         browser.close()

# test_valid_login()

# def test_valid_login(page: Page, site_url: str, valid_credentials: dict):

#     # ---- ARRANGE: Go to the login page ----
#     page.goto(site_url)

#     # ---- ACT: fill the form and submit -----
#     page.get_by_placeholder("Username").fill(valid_credentials["username"])
#     page.get_by_placeholder("Password").fill(valid_credentials["password"])
#     page.get_by_role("button", name= "Login").click()

#     # ---- ASSERT: Did we land on the product page? ----
#     expect(page).to_have_url(f"{site_url}/inventory.html")
#     expect(page.get_by_text("Products")).to_be_visible()

# def test_valid_login(page: Page):

#     login_page = LoginPage(Page)
#     login_page.load()
#     login_page.login("standard_user", "secret_sauce")
#     expect(page).to_have_url("https://www.saucedemo.com/inventory.html")


    #expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# def test_invalid_login(page: Page, invalid_credentials: dict):
#     login_page = LoginPage(page)

#     login_page.load()

#     login_page.login(invalid_credentials["username"], invalid_credentials["password"])

#     error = login_page.error_message()

#     print(error)

#     assert "Username and password do not match" in error

def test_inventory_page(page: Page, valid_credentials: dict):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()

    login_page.login(valid_credentials["username"], valid_credentials["password"])

    inventory_page.page_title()

    inventory_page.product_load()

    inventory_page.add_to_cart()

    inventory_page.remove_from_cart()
    

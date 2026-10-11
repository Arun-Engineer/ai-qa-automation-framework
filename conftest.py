import pytest
#from playwright.sync_api import sync_playwright

@ pytest.fixture(scope = "session")
def auth_state(browser):
    #with sync_playwright() as p:
        #browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        # log in once
        page.goto("https://www.saucedemo.com")
        page.get_by_placeholder("username").fill("standard_user")
        page.get_by_placeholder("password").fill("secret_sauce")
        page.get_by_role("button", name = "Login").click()

        # SAVE the session to a file
        context.storage_state(path = "auth.json")
        context.close()
        return "auth.json"

# @pytest.fixture
# def base_url() -> str:
#     """The site under test - defined once, used by every test."""
#     return "https://www.saucedemo.com"

@pytest.fixture
def valid_credentials() -> dict:
    """Real login data -kept here, not scattered across test files."""
    return {"username": "standard_user", "password": "secret_sauce"}

@pytest.fixture
def invalid_credentials() -> dict:
    """Invalid login data"""
    return {"username": "stand_user", "password": "secret_sauce"}
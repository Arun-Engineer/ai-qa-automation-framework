# pages/login_page.py
from playwright.sync_api import sync_playwright, Page, expect

class LoginPage:
    def __init__(self, page: Page):
        # store the page so all methods can use it
        self.page = page

        # ---- Locators: defined ONCE, here ------
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name = "Login")
        self.error_message_locator = page.locator("[data-test='error']")

    # ---- METHODS: actions on this page -----

    def load(self):
        """Navigate to the login page."""
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str):
        """Fill credentials and click login"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def error_message(self):
        return self.error_message_locator.inner_text()
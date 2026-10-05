from playwright.sync_api import sync_playwright, Page, expect
# Drill 1: Add a method to the loginpage called get_error_message() that returns the text of the error shown on a failed login.

# class LoginPage:
#     def __init__(self, page: Page):

#         self.page = page

#         self.username_input = page.get_by_placeholder("username")
#         self.password_input = page.get_by_placeholder("password")
#         self.login_button = page.get_by_role("button", name = "Login")
#         self.error_message = page.locator("[data-test='error']")

#     def load_page(self):
#         self.page.goto("https://www.saucedemo.com")

#     def login(self, username: str, password: str):

#         self.username_input.fill(username)
#         self.password_input.fill(password)
#         self.login_button.click()

#     def get_error_message(self):
#         return self.error_message

# Drill 2: Write a new test test_invalid_login that uses your page object to attempt login with
        # wrong_user/ "wrong_pass", then asserts the error message is visible.

class LoginPage:
    
    def __init__(self, page: Page):

        self.page = page

        self.username_input = page.get_by_placeholder("username")
        self.password_input = page.get_by_placeholder("password")
        self.login_button = page.get_by_role("button", name = "Login")
        self.error_message_locator = page.locator("[data-test='error']")
    
    def load_page(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
    
    def error_message(self):
        return self.error_message_locator.inner_text()
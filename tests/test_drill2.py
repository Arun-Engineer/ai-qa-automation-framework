from playwright.sync_api import Page
from dsa_interview_prep.drills.drills_2 import LoginPage


# def test_valid_login(page: Page):

#     login_page = LoginPage(page)

#     login_page.load_page()

#     login_page.login("stand_user", "secret")

#     error = login_page.get_error_message()

#     print(error)

def test_invalid_login(page: Page, invalid_credentials: dict):
    login_page = LoginPage(page)

    login_page.load_page()

    login_page.login(invalid_credentials["username"], invalid_credentials["password"])

    error = login_page.error_message()

    print(error)

    assert "Username and password do not match" in error
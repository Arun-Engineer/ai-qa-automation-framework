import pytest

@pytest.fixture
def site_url() -> str:
    """The site under test - defined once, used by every test."""
    return "https://www.saucedemo.com"

@pytest.fixture
def valid_credentials() -> dict:
    """Real login data -kept here, not scattered across test files."""
    return {"username": "standard_user", "password": "secret_sauce"}
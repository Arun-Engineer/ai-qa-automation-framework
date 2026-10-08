from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.first_name = page.get_by_placeholder("First Name")
        self.last_name = page.get_by_placeholder("Last Name")
        self.postal_code = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.get_by_role("button", name = "Finish")
        self.confirmation = page.locator(".complete-header")

    # Methods
    def fill_info(self, first: str, last: str, zip_code: str):
        """Fill the checkout form with customer info."""
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(zip_code)
        self.continue_button.click()

    def finish(self):
        """complete the order."""
        self.finish_button.click()

    def get_confirmation_message(self) -> str:
        """Return the order confirmation text(test asserts on it)."""
        return self.confirmation.inner_text()

    
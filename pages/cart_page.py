from playwright.sync_api import Page

class CartPage:
    def __init__(self, page: Page):
        self.page = page
        # LOCATORS
        self.checkout_button = page.get_by_role("button", name = "checkout")
        self.cart_items = page.locator(".cart_item")

    # Methods
    def checkout(self):
        """Click the checkout button."""
        self.checkout_button.click()

    def get_item_count(self):
        """Return how many items are in the cart."""
        return self.cart_items.count()

    
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout(page: Page, valid_credentials: dict):
    # Create all page objects
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    # Step 1: Login
    login_page.load()
    login_page.login(valid_credentials["username"], valid_credentials["password"])

    # Step 2: add a product to cart
    inventory_page.add_to_cart("Backpack")

    # Step 3: go to the cart (click cart icon)
    inventory_page.go_to_cart()

    # Step 4: click checkout
    cart_page.checkout()

    # Step 5: fill checkout_info
    checkout_page.fill_info("Sam", "kid", "600000")

    # Step 6: finish the order
    checkout_page.finish()

    # Step 7: Assert confirmation (the test asserts!)
    message = checkout_page.get_confirmation_message()
    assert "Thank you for your order" in message
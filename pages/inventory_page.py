from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page:Page):

        self.page = page

        self.title = page.locator(".title")
        self.products_loaded = page.locator(".inventory_list")
        self.products = page.locator(".inventory_item").filter(has_text = "Backpack")

    def page_title(self):
        expect(self.title).to_have_text("Products")

    def product_load(self):
        return self.products_loaded.is_visible()

    def add_to_cart(self):

        products_count = self.products.count()

        for i in range(products_count):
            product = self.products.nth(i)
            add_cart = product.get_by_role("button", name = "Add to cart")
            expect(add_cart).to_be_enabled()
            add_cart.click()

            remove_from_cart = product.get_by_role("button", name = "Remove")
            expect(remove_from_cart).to_be_visible()

    def remove_from_cart(self):
        products_count = self.products.count()
        
        for i in range(products_count):
            product = self.products.nth(i)
            remove_from_cart = product.get_by_role("button", name = "Remove")
            expect(remove_from_cart).to_be_visible()            
            remove_from_cart.click()

            add_cart = product.get_by_role("button", name = "Add to cart")
            expect(add_cart).to_be_enabled()
            
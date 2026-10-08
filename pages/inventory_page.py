from playwright.sync_api import Page, expect

class InventoryPage:
    def __init__(self, page:Page):

        self.page = page

        self.title = page.locator(".title")
        self.products_loaded = page.locator(".inventory_list")
        self.products = page.locator(".inventory_item")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort = page.locator(".Price (low to high)")

    def page_title(self):
        expect(self.title).to_have_text("Products")

    def product_load(self):
        return self.products_loaded.is_visible()

    def sort_products_by_price_low_high(self, page):
        self.sort.select_option("Price (low to high)")
        price = page.locator(label = ".inventory_item_price")
        first_price = price.nth(0).inner_text()
        second_price = price.nth(1).inner_text()

        first = float(first_price.replace("$", ""))
        second = float(second_price.replace("$", ""))

        assert first <= second


    def add_to_cart(self, product_name: str):
        self.products.filter(has_text = product_name).get_by_role("button", name = "Add to cart").click()

    def add_all_to_cart(self):

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

    def go_to_cart(self):

        self.cart_link.click()
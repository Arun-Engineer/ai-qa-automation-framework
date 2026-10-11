from playwright.sync_api import Page

def test_ui_handles_server_error(page: Page):
    def fail_with_500(route):
        route.fulfill(
            status = 500
        )
    page.route("**/api/**", fail_with_500)
    page.goto("https://example.com")
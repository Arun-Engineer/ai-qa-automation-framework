from playwright.sync_api import Page, expect

def test_mocked_api_response(page: Page):

    # Step 1: set up interception BEFORE navigation
    def handle_route(route):
        # Return our OWN fake response instead of the real backend
        route.fulfill(
            status = 200,
            content = "application/json",
            body = '{"message": "fake data"}',
        )

    # Catch ALL requests to any URL ending in /api/* and handle them
    page.route("**/api/**", handle_route)

    # Step 2: now navigate - any/api/call gets YOUR fake response
    page.goto("https://example.com")
    
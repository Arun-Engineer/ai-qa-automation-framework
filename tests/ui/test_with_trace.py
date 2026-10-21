from playwright.sync_api import Page, expect

def test_login_with_trace(page: Page, context):
    # START tracing - capture screenshots + snapshots + sources
    context.tracing.start(screenshots = True, snapshots = True, sources = True)

    # ---- the actual test ----
    page.goto("https://www.saucedemo.com")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name = "Login").click()
    expect(page.get_by_text("Products")).to_be_visible()

    # STOP racing - save to a zip file
    context.tracing.stop(path = "trace.zip")
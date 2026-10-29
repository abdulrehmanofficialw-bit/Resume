from playwright.sync_api import Page, expect


def test_homepage_has_expected_title_and_heading(page: Page, demo_url: str):
    page.goto(demo_url)
    expect(page).to_have_title("QA Demo Shop")
    expect(page.get_by_role("heading", name="QA Demo Shop")).to_be_visible()


def test_product_can_be_added_to_cart(page: Page, demo_url: str):
    page.goto(demo_url)
    page.get_by_role("button", name="Add to cart").click()
    expect(page.get_by_role("status").first).to_have_text("1 item in your cart.")


def test_password_field_is_masked(page: Page, demo_url: str):
    page.goto(demo_url)
    expect(page.locator("#password")).to_have_attribute("type", "password")


def test_invalid_login_shows_validation_message(page: Page, demo_url: str):
    page.goto(demo_url)
    page.locator("#username").fill("wrong-user")
    page.locator("#password").fill("wrong-password")
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator("#login-message")).to_have_text("Invalid username or password.")


def test_demo_login_succeeds_with_demo_credentials(page: Page, demo_url: str):
    page.goto(demo_url)
    page.locator("#username").fill("demo")
    page.locator("#password").fill("playwright-demo")
    page.get_by_role("button", name="Sign in").click()
    expect(page.locator("#login-message")).to_have_text("Signed in successfully.")


def test_price_is_present_and_numeric(page: Page, demo_url: str):
    page.goto(demo_url)
    price = page.locator("#price")
    expect(price).to_be_visible()
    assert float(price.get_attribute("data-price")) > 0

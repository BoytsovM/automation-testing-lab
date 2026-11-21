from playwright.sync_api import Page, expect


def test_login_page_is_displayed(page: Page) -> None:
    """Login form shows username, password, and the login button."""
    page.goto("https://www.saucedemo.com/")

    expect(page.locator('[data-test="username"]')).to_be_visible()
    expect(page.locator('[data-test="password"]')).to_be_visible()
    expect(page.locator('[data-test="login-button"]')).to_be_visible()


def test_successful_login(page: Page) -> None:
    """standard_user with secret_sauce opens the product catalog."""
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/incorrect.html")
    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()


def test_add_product_to_cart(page: Page) -> None:
    """Adding Sauce Labs Backpack sets the cart badge to 1."""
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="inventory-container"]')).to_be_visible()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")


def test_product_is_displayed_in_cart(page: Page) -> None:
    """The backpack added from the catalog is visible on the cart page."""
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")
    page.locator('[data-test="login-button"]').click()

    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()

    expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("1")

    page.locator('[data-test="shopping-cart-link"]').click()

    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()


def test_login_with_invalid_password(page: Page) -> None:
    """A wrong password stays on the login page and shows an error."""
    page.goto("https://www.saucedemo.com/")

    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("wrong_password")
    page.locator('[data-test="login-button"]').click()

    expect(page.locator('[data-test="error"]')).to_be_visible()
    expect(page.locator('[data-test="error"]')).to_contain_text(
        "Username and password do not match"
    )

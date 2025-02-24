import pytest


@pytest.fixture(autouse=True)
def reset_db(page):
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()
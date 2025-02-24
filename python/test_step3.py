import time

from playwright.sync_api import expect


def test_update_address(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    address_line_1 = "a"
    address_line_2 = "b"
    address_line_1_update = "a_updated"
    address_line_2_update = "b_updated"

    # Go to home page
    page.goto("https://e.lsi2.hr.dmerej.info/add_employee")

    # Create an employee
    page.locator('input[name="name"]').fill("a")
    page.locator('input[name="email"]').fill("a@b.fr")
    page.locator('input[name="address_line1"]').fill(address_line_1)
    page.locator('input[name="address_line2"]').fill(address_line_2)
    page.locator('input[name="city"]').fill("c")
    page.locator('input[name="zip_code"]').fill("27130")
    page.locator('input[name="hiring_date"]').fill("2002-08-30")
    page.locator('input[name="job_title"]').fill("d")
    page.get_by_role("button", name="Add").click()

    # Edit an employee
    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update address").click()
    expect(page.locator('input[name="address_line1"]')).to_have_value(address_line_1)
    expect(page.locator('input[name="address_line2"]')).to_have_value(address_line_2)
    page.locator('input[name="address_line1"]').fill(address_line_1_update)
    page.locator('input[name="address_line2"]').fill(address_line_2_update)
    page.get_by_role("button", name="Update").click()

    # Check that the values are saved CORRECTLY
    page.get_by_role("link", name="Update address").click()
    expect(page.locator('input[name="address_line1"]')).to_have_value(address_line_1_update)
    expect(page.locator('input[name="address_line2"]')).to_have_value(address_line_2_update)


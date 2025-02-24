import time

import pytest
from py_fixtures import reset_db
from playwright.sync_api import expect


def test_update_hiring_date(page):
    hiring_date = "2002-08-30"
    hiring_date_updated = "2022-07-10"

    # Create an employee
    page.goto("https://e.lsi2.hr.dmerej.info/add_employee")
    page.locator('input[name="name"]').fill("a")
    page.locator('input[name="email"]').fill("a@b.fr")
    page.locator('input[name="address_line1"]').fill("zzz")
    page.locator('input[name="address_line2"]').fill("www")
    page.locator('input[name="city"]').fill("c")
    page.locator('input[name="zip_code"]').fill("27130")
    page.locator('input[name="hiring_date"]').fill(hiring_date)
    page.locator('input[name="job_title"]').fill("d")
    page.get_by_role("button", name="Add").click()

    # Edit an employee
    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update contract").click()
    expect(page.locator('input[name="hiring_date"]')).to_have_value(hiring_date)

    # Le champ semble être devenu non-editable, donc le test n'est plus pertinent
    page.locator('input[name="hiring_date"]').fill(hiring_date_updated)
    page.get_by_role("button", name="Update").click()

    # Check that the values are saved CORRECTLY
    page.get_by_role("link", name="Update contract").click()
    expect(page.locator('input[name="hiring_date"]')).to_have_value(hiring_date_updated)


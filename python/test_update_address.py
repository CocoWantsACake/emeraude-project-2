from playwright.sync_api import expect

from employee import Employee


def test_update_address(page):
    empl_factory = Employee(page)

    address_line_1 = "a"
    address_line_2 = "b"
    address_line_1_update = "a_updated"
    address_line_2_update = "b_updated"

    # Create an employee
    empl_factory.navigate_create()
    empl_factory.create_employee(
        name="a",
        email="a@b.fr",
        address_line_1=address_line_1,
        address_line_2=address_line_2,
        city="c",
        zip_code="27130",
        hiring_date="2002-08-30",
        job_title="d"
    )

    # Edit an employee
    empl_factory.navigate_list()
    empl_factory.open_edition_employee(
        name="a",
        email="a@b.fr"
    )

    # page.get_by_role("link", name="Edit").click()
    # page.get_by_role("link", name="Update address").click()
    expect(page.locator('input[name="address_line1"]')).to_have_value(address_line_1)
    expect(page.locator('input[name="address_line2"]')).to_have_value(address_line_2)
    page.locator('input[name="address_line1"]').fill(address_line_1_update)
    page.locator('input[name="address_line2"]').fill(address_line_2_update)
    page.get_by_role("button", name="Update").click()

    # Check that the values are saved CORRECTLY
    page.get_by_role("link", name="Update address").click()
    expect(page.locator('input[name="address_line1"]')).to_have_value(address_line_1_update)
    expect(page.locator('input[name="address_line2"]')).to_have_value(address_line_2_update)


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
    test = page.locator('textbox[name="Name"]')
    test.fill("a")

    page.locator('input[name="Email"]').fill("a@b.fr")
    page.locator("#id_address_line1").fill(address_line_1)
    page.locator("#id_address_line2").fill(address_line_2)
    page.locator('input[name="City"]').fill("c")
    page.locator('input[name="Zip code"]').fill("27130")
    page.locator('input[name="Hiring date"]').fill("2002-08-30")
    page.locator('input[name="Job title"]').fill("d")
    page.locator('button[name="Add"]').click()

    # Edit an employee
    page.locator('button[name="Edit"]').click()
    expect(page.locator("#id_address_line2")).to_contain_text(address_line_1)
    expect(page.locator("#id_address_line2")).to_contain_text(address_line_2)
    page.locator("#id_address_line1").fill(address_line_1_update)
    page.locator("#id_address_line2").fill(address_line_2_update)
    page.locator('button[name="Update"]').click()

    # Check that the values are saved CORRECTLY UWU
    page.locator('button[name="Edit"]').click()
    expect(page.locator("#id_address_line2")).to_contain_text(address_line_1_update)
    expect(page.locator("#id_address_line2")).to_contain_text(address_line_2_update)


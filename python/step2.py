import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.lsi2.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("a")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("a@b.fr")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("a")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("b")
    page.get_by_role("textbox", name="City").click()
    page.get_by_role("textbox", name="City").fill("c")
    page.get_by_role("spinbutton", name="Zip code").click()
    page.get_by_role("spinbutton", name="Zip code").fill("27130")
    page.get_by_role("textbox", name="Hiring date").fill("2002-08-30")
    page.get_by_role("textbox", name="Job title").click()
    page.get_by_role("textbox", name="Job title").fill("d")
    page.get_by_role("button", name="Add").click()
    page.get_by_role("link", name="Edit").click()
    page.get_by_role("link", name="Update address").click()
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("aaaa")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("bbbb")
    page.get_by_role("button", name="Update").click()
    page.get_by_role("link", name="Update address").click()
    expect(page.locator("#id_address_line2")).to_be_visible()
    expect(page.locator("#id_address_line2")).to_contain_text("bbbb")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

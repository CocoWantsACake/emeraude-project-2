class Employee:
    page = None

    def __init__(self, page):
        self.page = page

    def navigate_create(self):
        self.page.goto("/add_employee")

    def navigate_list(self):
        self.page.goto("/list_employee")


def create_employee(page, name, email, address_line_1, address_line_2, city, zip_code, hiring_date, job_title):
    create_employee(page)
    page.locator('input[name="name"]').fill(name)
    page.locator('input[name="email"]').fill(email)
    page.locator('input[name="address_line1"]').fill(address_line_1)
    page.locator('input[name="address_line2"]').fill(address_line_2)
    page.locator('input[name="city"]').fill(city)
    page.locator('input[name="zip_code"]').fill(zip_code)
    page.locator('input[name="hiring_date"]').fill(hiring_date)
    page.locator('input[name="job_title"]').fill(job_title)
    page.get_by_role("button", name="Add").click()


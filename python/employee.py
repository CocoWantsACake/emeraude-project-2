class Employee:
    page = None

    def __init__(self, page):
        self.page = page

    def navigate_create(self):
        self.page.goto("/add_employee")

    def navigate_list(self):
        self.page.goto("/employees")

    def create_employee(self, name, email, address_line_1, address_line_2, city, zip_code, hiring_date, job_title):
        self.page.locator('input[name="name"]').fill(name)
        self.page.locator('input[name="email"]').fill(email)
        self.page.locator('input[name="address_line1"]').fill(address_line_1)
        self.page.locator('input[name="address_line2"]').fill(address_line_2)
        self.page.locator('input[name="city"]').fill(city)
        self.page.locator('input[name="zip_code"]').fill(zip_code)
        self.page.locator('input[name="hiring_date"]').fill(hiring_date)
        self.page.locator('input[name="job_title"]').fill(job_title)
        self.page.get_by_role("button", name="Add").click()

    """
    Definir les fonctions uniques pour chaque "fill" des fonctions ci-dessus.
    """

    def open_edition_employee(self, name, email):
        """
        Opens the edition panel of the employee defined by the given name and email
        """
        row = self.page.locator(f'xpath=//tr[td[text()="{name}"] and td[text()="{email}"]]')

        if row.count() > 0:
            edit_button = row.locator('a.btn.btn-primary:has-text("Edit")')
            edit_button.click()
        else:
            print(f"Aucune ligne trouvée pour le nom '{name}' et l'email '{email}'.")

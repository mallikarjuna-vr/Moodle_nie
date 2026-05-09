from playwright.sync_api import Page, expect
from utilites.ConfigReader import ConfigReader

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.dropdown_button = page.get_by_role("button", name="Display drop-down menu")
        self.select_summary = page.get_by_role("link", name="Switch to summary view")
        self.select_course = page.get_by_label("Course overview", exact=True).get_by_role("link", name="Computer Networks - 2025-26 - A sec")

    def navigate_to_course(self):
        try:
            self.dropdown_button.click()
            self.select_summary.click()
            self.select_course.click()
            config = ConfigReader()
            course_url = config.readConfig("basic info","courseURL")
            self.page.wait_for_url(course_url)
            expect(self.page).to_have_url(course_url)
        except:
            print("Failed to navigate to course page.")

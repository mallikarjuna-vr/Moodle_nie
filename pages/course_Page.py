from playwright.sync_api import Page, expect
from utilites.ConfigReader import ConfigReader

class CoursePage:
    def __init__(self, page: Page):
        self.page = page
        self.upload_page_link =  page.locator("//a[contains(.,'CISCO Network academy file submission')]")

    def navigate_to_upload_page(self):
        try:
            self.upload_page_link.click()
            config = ConfigReader()
            upload_url = config.readConfig("basic info","uploadURL")
            self.page.wait_for_url(upload_url)
            expect(self.page).to_have_url(upload_url)
        except:
            print("Failed to navigate to upload page.")
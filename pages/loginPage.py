
from playwright.sync_api import Page, expect
from utilites.ConfigReader import ConfigReader


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.frist_login_click = page.locator("//span[@class='login']/a")
        self.username_textField = page.get_by_placeholder("Username")
        self.password_textField = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Log in", exact=True)

    def login_to_application(self, username, password):
        try:
            self.frist_login_click.click()
            self.username_textField.fill(username)
            self.password_textField.fill(password)
            self.login_button.click()
            config_reader = ConfigReader()
            dashboard_URL = config_reader.readConfig("basic info" , "dashboardURL")
            self.page.wait_for_url(dashboard_URL)
            expect(self.page).to_have_url(dashboard_URL)
        except:
            print("Login failed, please check your credentials and try again.")
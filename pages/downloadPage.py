from playwright.sync_api import Page
import os


class DownloadPage:

    def __init__(self, page: Page):
        self.page = page
        self.download_button = page.locator("(//a[@target='_blank'])[1]")

    def navigate_to_download_page(self):
        try:
            with self.page.expect_download() as download_info:
                self.download_button.click()

            download = download_info.value

            folder_path = r"C:\Users\malli\Downloads\coursers_certificates"
            os.makedirs(folder_path, exist_ok=True)

            file_path = os.path.join(folder_path, download.suggested_filename)

            download.save_as(file_path)

            print("File saved at:", file_path)

        except:
            print("Failed to download file:")

    def logout(self):
        try:
            self.page.get_by_role("button", name="User menu").click()
            self.page.get_by_role("menuitem", name="Log out").click()
        except:
            print("Failed to log out.")
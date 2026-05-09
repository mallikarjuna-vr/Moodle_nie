
import os
from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False,slow_mo=1000)

    context = browser.new_context(accept_downloads=True)
    page = context.new_page()

    page.goto("https://moodlegurukul.nie.ac.in/")
    page.locator("//span[@class='login']/a").click()
    page.get_by_role("textbox", name="Username").fill("2023ec_adarshr_a@nie.ac.in")
    page.get_by_role("textbox", name="Password").fill("Moodle@123")
    page.get_by_role("button", name="Log in", exact=True).click()
    page.get_by_role("button", name="Display drop-down menu").click()
    page.get_by_role("link", name="Switch to summary view").click()
    page.get_by_label("Course overview", exact=True).get_by_role("link", name="Computer Networks - 2025-26 - A sec").click()
    page.locator("//a[contains(.,'CISCO Network academy file submission')]").click()

    with page.expect_download() as download_info:
        with page.expect_popup() as popup_info:
            page.locator("(//a[@target='_blank'])[1]").click()

        popup_page = popup_info.value
        download = download_info.value

    # Your folder path
    folder_path = r"C:\Users\malli\Downloads\cn"

    # Create folder if not exists
    os.makedirs(folder_path, exist_ok=True)

    # Save file with same name
    file_path = os.path.join(folder_path, download.suggested_filename)
    download.save_as(file_path)

    print("File saved at:", file_path)

    popup_page.close()

    page.get_by_role("button", name="User menu").click()
    page.get_by_role("menuitem", name="Log out").click()

    context.close()
    browser.close()



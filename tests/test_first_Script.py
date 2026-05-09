import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.course_Page import CoursePage
from pages.downloadPage import DownloadPage
from utilites.ExcelData import ExcelData

class Test_E2Escenierio1:

    def test_fristScript(self, page):
        login_page = LoginPage(page)
        home_page = HomePage(page)
        course_page = CoursePage(page)
        download_page = DownloadPage(page)
        excel_data = ExcelData()
        rows = excel_data.getRowCount(
            "testData/moodle_datasheet.xlsx",
            "Sheet1"
        )

        for row in range(2, rows + 1):
            username = excel_data.getCellData(
                "testData/moodle_datasheet.xlsx",
                "Sheet1",
                row,
                1
            )

            password = excel_data.getCellData(
                "testData/moodle_datasheet.xlsx",
                "Sheet1",
                row,
                2
            )
            print(f"Running for user: {username}")
            login_page.login_to_application(username,password)
            home_page.navigate_to_course()
            course_page.navigate_to_upload_page()
            download_page.navigate_to_download_page()
            download_page.logout()

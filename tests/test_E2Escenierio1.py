from pages.loginPage import LoginPage
from pages.homePage import HomePage
from pages.course_Page import CoursePage
from pages.downloadPage import DownloadPage
from utilites.ExcelData import ExcelData

def test_fristScript(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    course_page = CoursePage(page)
    download_page = DownloadPage(page)
    excel_data = ExcelData()
    username = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 1)
    password = excel_data.getCellData("testData/userInfo.xlsx", "Sheet1", 2, 2)

    login_page.login_to_application(username,password)
    home_page.navigate_to_course()
    course_page.navigate_to_upload_page()
    download_page.navigate_to_download_page()
    download_page.logout()
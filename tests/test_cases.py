from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time
from selenium.webdriver.chrome.options import Options


class TestCases():
    @pytest.fixture()
    def setUp(self) -> None:
        options = Options()
        options.add_argument("--start-fullscreen")
        self.driver = webdriver.Chrome(
            executable_path="/home/mdyamin/Files/Internship/Web-Automation/facebook-messenger-bot-selenium/chromedriver")
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(300)
        yield
        self.driver.close()

    def test_1(self, setUp):
        page_1 = LoginPage(driver=self.driver)
        page_1.open('')
        time.sleep(5)
        page_1.scroll_down()
        time.sleep(5)
        page_1.login("hexibo6791@0ranges.com", "yamin787898")
        time.sleep(10)
        page_2 = HomePage(driver=self.driver)
        page_2.send_message('hello')
        time.sleep(5)





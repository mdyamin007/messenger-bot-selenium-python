from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.home_page import HomePage
import time

class TestCases():
    @pytest.fixture()
    def setUp(self) -> None:
        self.driver = webdriver.Firefox(
            executable_path="/home/mdyamin/Files/Internship/Web-Automation/facebook-messenger-bot-selenium/geckodriver")
        yield
        self.driver.close()

    def test_1(self, setUp):
        page_1 = LoginPage(driver=self.driver)
        page_1.open('')
        time.sleep(5)
        page_1.login("hexibo6791@0ranges.com", "yamin787898")
        time.sleep(10)
        page_2 = HomePage(driver=self.driver)
        page_2.send_message('demo')
        # page_2.click_on_messenger_icon()





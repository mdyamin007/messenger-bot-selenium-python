from pages.base_page import BasePage
from utils.locators import HomePageLocators
import time
from selenium.webdriver.common.by import By

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def send_message(self, message):
        persons = (self.driver.find_element(*self.locator.PERSONS)).find_elements(*self.locator.PERSON)
        for person in persons:
            time.sleep(3)
            person.click()
            time.sleep(5)
            msg = self.driver.find_element(*self.locator.MESSAGE_TXTBOX)
            time.sleep(5)
            msg.send_keys(message)
            time.sleep(3)
            print("message sent")
            send_button = self.driver.find_element(*self.locator.SEND_BUTTON)
            send_button.click()
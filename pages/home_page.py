from pages.base_page import BasePage
from utils.locators import HomePageLocators

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HomePageLocators

    def click_on_person(self):
        person_1 = self.driver.find_element(*self.locator.PERSON_1)
        person_1.click()
    
    def send_message(self, message):
        self.driver.execute_script(f"document.evaluate('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/span/span', document, null).singleNodeValue.innerHTML = {message};") 
        # message_txtbox = self.driver.find_element(*self.locator.MESSAGE_TXTBOX)
        # message_txtbox.click()
        # message_txtbox.send_keys(message)
        send_button = self.driver.find_element(*self.locator.SEND_BUTTON)
        send_button.click()
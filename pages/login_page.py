from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = LoginPageLocators

    def login(self, email, password):
        email_txtbox = self.driver.find_element(*self.locator.EMAIL_TEXTBOX)
        password_txtbox = self.driver.find_element(*self.locator.PASSWORD_TEXTBOX)
        login_button = self.driver.find_element(*self.locator.LOGIN_BUTTON)
        email_txtbox.click()
        email_txtbox.send_keys(email)
        password_txtbox.click()
        password_txtbox.send_keys(password)
        login_button.click()
        


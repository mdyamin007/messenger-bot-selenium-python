from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL_TEXTBOX = (By.ID, 'email')
    PASSWORD_TEXTBOX = (By.ID, 'pass')
    LOGIN_BUTTON = (By.ID, 'loginbutton')

class HomePageLocators(object):
    PERSON_1 = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div/div[1]/div/a/div/div[2]/div[1]')
    MESSAGE_TXTBOX = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div/div/div/div')
    SEND_BUTTON = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div/div[2]/div/form/div/div[3]/span[2]/div/svg')

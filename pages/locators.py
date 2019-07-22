from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "[value = 'Log In']")
    REGISTER_FROM = (By.CSS_SELECTOR, "[value = 'Register']")
#Страница с логином
from .base_page import BasePage
from .locators import *
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Login don't in URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FROM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        email_el = self.browser.find_element(*BasePageLocators.EMAIL_FIELD).send_keys(email)
        pas_el = self.browser.find_element(*BasePageLocators.REG_PAS).send_keys(password)
        pas_el = self.browser.find_element(*BasePageLocators.REG_PAS2).send_keys(password)
        button = self.browser.find_element_by_css_selector("button[name ='registration_submit'").click()
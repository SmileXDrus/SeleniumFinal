#Главная страница
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    
    def open_busket(self):
        link = self.browser.find_element_by_css_selector(".hidden-xs > span > a")
        link.click()
        
    def no_product(self):
        assert self.is_element_present(*MainPageLocators.NO_PRODUCT), "Product in the busket"
'''
    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click() 
       
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
'''
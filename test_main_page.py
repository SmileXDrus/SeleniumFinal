#Тест по страницам товаров и логина
import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
import time

    #TEST Проверка на переход на страницу регистрации
@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link) # инициализируем Page Object
        page.open()
        page.go_to_login_page() 
    
    #TEST Проверка на наличие ссылки на регистрацию
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link, 1)
        page.open()
        page.should_be_login_link()
    
    #Переход на страницу логина
@pytest.mark.skip
def go_to_login_page(self):
    link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    link.click()
    #return LoginPage(self.browser, self.browser.current_url)
    
    #TEST Проверка на странице логина наличие форм регистрации и входа
@pytest.mark.skip
def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.skip    
def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = CartPage(browser, link)
    page.open()
    page.open_busket()
    #time.sleep(15)
    page.no_product_in_the_busket_message()
    page.no_product_in_the_busket()
    
    
# Запуск pytest -v --tb=line  --language=en test_main_page.py
# ЗАпуск2 pytest -v --tb=line -m login_guest --language=en test_main_page.py

#Тест

from .pages.main_page import MainPage
from .pages.login_page import LoginPage

    #Проверка на переход на страницу регистрации
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link) # инициализируем Page Object
    page.open()
    page.go_to_login_page() 
    
    #Проверка на наличие ссылки на регистрацию
def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link, 1)
    page.open()
    page.should_be_login_link()

def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    
# Запуск pytest -v --tb=line --language=en test_main_page.py

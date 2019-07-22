#Тест

from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object
    page.open()
    page.go_to_login_page()   
    
# Запуск pytest -v --tb=line --language=en test_main_page.py

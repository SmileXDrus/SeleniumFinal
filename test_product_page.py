#Тесты по странице продукта
import pytest
from .pages.product_page import ProductPage

numbers = [
"0","1","2","3","4","5","6","7","8","9"
]


#TEST добавления в корзину и получения контрольной суммы
@pytest.mark.parametrize("url", numbers)
def test_guest_can_add_product_to_cart(url, browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    link = f"{product_base_link}/?promo=offer{url}"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.solve_quiz_and_get_code()
    #page.should_be_right_name_and_price()

"""  
#TEST Проверка на наличие соответствие цены и наименования товара
def test_should_be_name_and_price(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_and_price()
"""    
#Запуск pytest -s test_product_page.py

    
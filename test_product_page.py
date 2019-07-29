#Тесты по странице продукта
import pytest
from .pages.product_page import ProductPage
import time
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage

numbers = [
"0","1","2","3","4","5","6","7","8","9"
]


#TEST добавления в корзину и получения контрольной суммы
@pytest.mark.parametrize("url", numbers)
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(url, browser):
    product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    link = f"{product_base_link}/?promo=offer{url}"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.solve_quiz_and_get_code()
    page.should_be_right_name()

#TEST1 Проверка наличия перехода на страницу авторизации
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

#TEST2 Проверка перехода на страницу авторизации
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#TEST1 С добавлением в корзину (is_not_element_present)
@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=0"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.should_not_be_success_message()

#TEST2 Без добавления в корзину (is_not_element_present)
@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=0"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    #page.put_in_basket()
    page.should_not_be_success_message()
	
#TEST3 С добавлением в корзину (is_disappeared)
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=0"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.should_not_be_success_message2()

#TEST Проверка на наличие соответствие наименования товара
@pytest.mark.skip
def test_should_be_right_name(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link) # инициализируем Page Object
    page.open()
    page.put_in_basket()
    page.solve_quiz_and_get_code()
    #time.sleep(10)
    page.should_be_right_name()

@pytest.mark.need_review	
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=0"
    page = CartPage(browser, link)
    page.open()
    page.open_busket()
    page.no_product_in_the_busket_message()
    page.no_product_in_the_busket()

    
class TestUserAddToCartFromProductPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(str(time.time()) + "@fakemail.org", '123qweCCC3')
        page.should_be_authorized_user()
        yield
        # teardown
    @pytest.mark.skip    
    def test_user_cant_see_success_message(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=0"
        page = ProductPage(browser, link) # инициализируем Page Object
        page.open()
        #page.put_in_basket()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(url, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link) # инициализируем Page Object
        page.open()
        page.put_in_basket()
        page.solve_quiz_and_get_code()
        page.should_be_right_name()    
#Запуск pytest -s test_product_page.py 
#pytest -v --tb=line --language=en test_product_page.py 
#pytest -v --tb=line --language=en -m need_review
    
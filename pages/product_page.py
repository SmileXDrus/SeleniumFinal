#Страница с продуктом

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def put_in_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT)
        basket_link.click()
        
    #Проверка на наименование    
    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "NAME_PRODUCT is not presented"
        
    #Проверка на цену
    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "PRICE_PRODUCT is not presented"

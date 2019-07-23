#Страница с продуктом

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def put_in_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT)
        basket_link.click()
    
    #Общая проверка соотвествия продукта (наименование и цена)
    def should_be_right_name_and_price(self):
        text = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert  text == "Coders at Work", "MISTAKE" 
    
        
'''       
    #Общая проверка налиция продукта (наименование и цена)
    def should_be_name_and_price(self):
        self.should_be_name_product()
        self.should_be_price_product()
        
    #Проверка налицие наименования   
    def should_be_name_product(self):
        assert self.is_element_present(*ProductPageLocators.NAME_PRODUCT), "NAME_PRODUCT is not presented"
        
    #Проверка налицие цены
    def should_be_price_product(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_PRODUCT), "PRICE_PRODUCT is not presented"
'''

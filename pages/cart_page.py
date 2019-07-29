from .locators import *
from .base_page import BasePage

class CartPage(BasePage):   
    #Проверка того, что есть сообщение об отсутствии товара
    def no_product_in_the_busket_message(self):
        assert self.is_element_present(*BusketPageLocators.NO_PRODUCT), "Product in the busket"
	
	#Проверка того, что товара нет	
    def no_product_in_the_busket(self):
        assert not self.is_element_present(*BusketPageLocators.BTN_GO_TO_CHECKOUT), "Product in the busket"

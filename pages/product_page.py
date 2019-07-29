#Страница с продуктом

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
        
    #Общая проверка соотвествия продукта (наименование)
    def should_be_right_name(self):
        textName = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        assert  textName == "Coders at Work"
    
	#Проверка на вывод сообщения об успехе
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be" 
	
	#Проверка на вывод сообщения об успехе
    def should_not_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"



'''	
#Наличие    
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
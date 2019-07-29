#Базовая страница
import math
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import *

class BasePage(object):
    def __init__(self, browser, url, timeout=10): #Конструктор
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    #Проверка на авторизованность
    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"	
    #Открытие корзины
    def open_busket(self):
        link = self.browser.find_element_by_css_selector(".hidden-xs > span > a")
        link.click() 
		
    #Переход на логинку
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()
		
    def should_be_login_link(self):
	    assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
	
    #Открытие браузера    
    def open(self):
        self.browser.get(self.url)
    
    #Обработка исключения (как искать и что искать )
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

	#абстрактный метод, который проверяет, что элемент не появляется на странице в течение заданного времени
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
        
    #Переход в корзину 
    def put_in_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT)
        basket_link.click()
		
	#Если же мы хотим проверить, что какой-то элемент исчезает
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
	
	
    #Считает результат математического выражения и вводит ответ
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
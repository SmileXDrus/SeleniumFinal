from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "[value = 'Log In']")
    REGISTER_FROM = (By.CSS_SELECTOR, "[value = 'Register']")

class ProductPageLocators(object):
    NAME_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")               
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".fade.in > div > p:nth-child(1) > strong")  
    BASKET_PRODUCT = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")
    
'''   
    NAME_PRODUCT_PREV = (By.CSS_SELECTOR, ".product_main > h1")
    PRICE_PRODUCT_PREV = (By.CSS_SELECTOR, ".product_main > p.price_color")
'''
	
class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
#Базовая страница


class BasePage(object):
    def __init__(self, browser, url): #Конструктор
        self.browser = browser
        self.url = url
        
    def open(self):
        self.browser.get(self.url)
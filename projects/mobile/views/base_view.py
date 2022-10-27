import datetime
import sys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseView():

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(30) # Обьявляем ожидания для страниц
        self.wait = WebDriverWait(self.driver, 30) # Указываем ожидания для элементов
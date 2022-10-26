import datetime
import os

from data.data import Data
from data.locators import Locators
from data.links import Links
from libs.helper import Helper
from libs.dbrequest import DbRequest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains



#########################################################################################
# В данном классе мы создаем страницу, __init__ которой будет подтягиваться во все pages
# А так же пишем общие функции, но лучше писать в файл pylex.py
#########################################################################################
class BasePage:

    #######################################################
    # Тут обьявляем общие параметры для тестов
    #######################################################
    def __init__(self, driver):
        self.driver = driver
        self.driver.set_window_size(1920, 1080)  # Указываем размер окна
        self.driver.set_page_load_timeout(60)
        self.wait = WebDriverWait(self.driver, 30, poll_frequency=1)
        self.helper = Helper(self.driver)
        # self.generators = Generators()
        # self.action = ActionChains(self.driver)
        # self.mail = Mailchecker()


        self.db = DbRequest()
        self.locators = Locators()
        self.data = Data()
        self.links = Links()

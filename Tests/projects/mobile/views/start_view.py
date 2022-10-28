import time
import allure
import appium
import os
import sys
from data.locators import Locators
from selenium.webdriver.common.by import By
from projects.mobile.views.base_view import BaseView
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
from selenium.webdriver.common.keys import Keys


class Start(BaseView):

    GETTING_STARTED_BUTTON = (By.XPATH, Locators.GETTING_STARTED_BUTTON)
    EMAIL_FIELD = (By.XPATH, Locators.EMAIL_FIELD)

    def click_on(self):
        self.driver.find_element(*self.GETTING_STARTED_BUTTON).click()
        time.sleep(10)

    def enter_email(self):
        self.driver.find_element(*self.EMAIL_FIELD).click()
        self.driver.find_element(*self.EMAIL_FIELD).send_keys("12314241")
        time.sleep(10)
    

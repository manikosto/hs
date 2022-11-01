import os

from projects.integration.pages.BasePage import BasePage
from libs.dbrequest import DbRequest
from libs.apirequest import ApiRequest
from requests.auth import HTTPBasicAuth
from config import Config
from selenium.webdriver.common.by import By
import time

class TasksPage(BasePage):
    
    def open_page(self): # Название шага
        self.helper.check_title(self.locators.HOME_TITLE) # Действие 1
        self.helper.highlight_element_by_xpath(self.locators.LOGO)
        self.helper.get_screenshot("Page is opened") # Действие 2
    
    def login_in_account(self):
        self.helper.send_keys_in_element_by_xpath(self.locators.EMAIL_FIELD, self.data.ACCOUNT_LOGIN)
        self.helper.send_keys_in_element_by_xpath(self.locators.PASSWORD_FIELD, self.data.ACCOUNT_PASSWORD)
        self.helper.click_on_element_by_xpath(self.locators.SUBMIT_BUTTON)
        self.helper.get_screenshot("Credentials are entered")
    
    def check_track_page(self):
        time.sleep(3)
        self.helper.highlight_element_by_xpath(self.locators.ALL_TRACKS_BUTTON)
        self.helper.get_screenshot("Credentials are entered")
    
    def open_next_section(self):
        self.helper.get_scroll_to_bottom()
        self.helper.click_on_element_by_xpath(self.locators.NEXT_SECTION_BUTTON)
        self.helper.get_scroll_to_bottom()
        # assert self.driver.find_element(By.XPATH, self.locators.SECTION_COUNTER).get_attribute("value") == " 7 sections left "


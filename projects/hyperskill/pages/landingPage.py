import os

from projects.integration.pages.BasePage import BasePage
from libs.dbrequest import DbRequest
from libs.apirequest import ApiRequest
from requests.auth import HTTPBasicAuth
from config import Config


class LandingPage(BasePage):
    
    def open_page(self): # Название шага
        self.helper.check_title(self.locators.HOME_TITLE) # Действие 1
        self.helper.highlight_element_by_xpath(self.locators.LOGO)
        self.helper.get_screenshot("Page is opened") # Действие 2
    
    # def get_subscriptions(self):
    #     with DbRequest() as db:
    #         self.helper.allure_attach_text(db.get_users())
    #         # db.select_subscription_by_email("akoledachkin@freeconferencecall.com")
    
    # def get_cat_fact(self):
    #     with ApiRequest() as ws:
    #         self.helper.allure_attach_json(ws.get_cat_fact())

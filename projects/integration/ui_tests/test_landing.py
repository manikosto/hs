import pytest
import allure
import requests
import os
import sys
from config import Config

from data.links import Links
from projects.integration.pages.landingPage import LandingPage
from libs.dbrequest import DbRequest
from requests.auth import HTTPBasicAuth
from libs.helper import Helper
# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


@pytest.mark.usefixtures("driver")
@allure.parent_suite("Landing")
@allure.suite("Landing page")
class Test_Landing:

    def setup(self):
        self.links = Links()
        self.landingPage = LandingPage(self.driver)
        self.driver.get(self.links.landing_page)
        

    @allure.title("Check successfull integration test")
    @allure.description("Check successfull integration test using UI, DB, API")
    @allure.severity("Critical")
    @allure.link(url="", name="")
    @pytest.mark.smoke
    def test_successfull_integration_test(self):

        with allure.step("UI step demonstration"):
            self.landingPage.check_open_page()

        # with allure.step("DB step demonstration"):
        #     self.landingPage.get_subscriptions()

        # with allure.step("API step demonstration"):
        #     self.landingPage.get_cat_fact()
                
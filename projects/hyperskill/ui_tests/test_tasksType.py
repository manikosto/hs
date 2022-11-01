import pytest
import allure
import requests
import os
import sys
from config import Config
import time
from data.links import Links
from projects.hyperskill.pages.tasks_page import TasksPage
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
        self.helper = Helper(self.driver)
        self.tasksPage = TasksPage(self.driver)
        self.driver.get(self.links.login_page)
        

    @allure.title("Login in account")
    @allure.description("Check successfull login in account")
    @allure.severity("Critical")
    @allure.link(url="", name="")
    @pytest.mark.smoke
    def test_successfull_login_test(self):

        with allure.step("Open login page"):
            self.tasksPage.open_page()
        
        with allure.step("Enter credentials"):
            self.tasksPage.login_in_account()
            self.helper.save_cookies("hyperskill_release")
        
        with allure.step("Check track page is opened"):
            self.tasksPage.check_track_page()
    
    @allure.title("Check successfull integration test")
    @allure.description("Check successfull integration test using UI, DB, API")
    @allure.severity("Critical")
    @allure.link(url="", name="")
    @pytest.mark.smoke1
    def test_theory_task(self):

        with allure.step("UI step demonstration"):
            self.helper.load_cookies(self.links.tasks["theory"], "hyperskill_release")
        
        with allure.step("UI step demonstration"):
            self.tasksPage.open_next_section()
        
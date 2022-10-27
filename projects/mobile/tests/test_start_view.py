
import allure
import pytest
import os
import appium
import sys
from projects.mobile.views.start_view import Start


@pytest.mark.usefixtures("driver")
@allure.parent_suite("Start")
@allure.suite("Start view")
class Test_Start():

    def setup(self):
        self.start_view = Start(self.driver)


    @allure.title("Check page openning")
    @allure.severity("Critical")
    @allure.link(url="https://app.qase.io/case/CP-5", name="QASE")
    @pytest.mark.sanity
    @pytest.mark.smoke 
    def test_check_click(self):
        
        with allure.step("Click continue"):
            self.start_view.click_on()
            
        
        # with allure.step("Click on profile button"):
        #     self.start_view.click_on_profile_button()
        

        # with allure.step("Click on login button"):
        #     self.start_view.click_on_login_button()
        
        with allure.step("Enter email"):
            self.start_view.enter_email()
        
        # with allure.step("Enter password"):
        #     self.start_view.enter_password()
        
        # with allure.step("Click authorize button"):
        #     self.start_view.click_on_authorized_button()
        
        # with allure.step("Check login"):
        #     self.start_view.check_correct_login()
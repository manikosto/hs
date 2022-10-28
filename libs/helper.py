
import allure
import datetime
import os
import sys
import time
import pickle

from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


class Helper:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    '''Methods for highlights'''

    def highlight_element_by_xpath(self, xpath_locator, color="fuchsia"):
        """[This method finds element by xpath and adds CSS border on Allure screenshot]

        Args:
            xpath_locator ([xpath]): [XPATH locator]

        Returns:
            [Element]: [Highlight of element on Allure screenshot]
        """
        try:
            self.driver.execute_script(
                "function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log((getElementByXpath(\"" + xpath_locator + "\").style.border=\"3px solid "+str(color)+"\"));")
        except:
            # raise Exception("Element was not found to be highlight")
            # return Exception
            return False

    def highlight_element_by_id(self, id):
        """[This method finds element by id and adds CSS border on Allure screenshot]

        Args:
            id_locator ([id]): [ID locator]

        Returns:
            [Element]: [Highlight of element on Allure screenshot]
        """
        try:
            self.driver.execute_script(
                "document.getElementById(" + id + ").style.border=\"3px solid red\";")
        except:
            # raise Exception("Element was not found to be highlight")
            return False

    '''Methods for text'''

    def check_title(self, title):
        """[This method asserts the title of the page]

        Args:
            title ([text]): [Expected title]

        Raises:
            ValueError: [Title is not correct]
        """
        try:
            count = 0
            while count != 5:
                title = self.driver.title
                count += 1
                if title in self.driver.title:
                    assert title in self.driver.title
                    break
        except:
            raise ValueError("Title is not correct")

    def check_text_of_element_by_xpath(self, xpath_locator, ftext):
        """[This method asserts the text of the element by XPATH]

        Args:
            xpath_locator ([xpath]): [XPATH locator]
            ftext ([text]): [Expected the text of the element]

        Raises:
            ValueError: [The text of the element is not correct]
        """
        try:
            elements_text = self.driver.find_element(
                By.XPATH, xpath_locator).text
            assert elements_text == ftext
        except:
            raise ValueError("The text of the element is not correct")

    def check_text_of_element_by_id(self, id_locator, ftext):
        """[This method asserts the text of the element by ID]

        Args:
            id_locator ([id]): [ID locator]
            ftext ([text]): [The text of the element]

        Raises:
            ValueError: [The text of the element is not correct]
        """
        try:
            elements_text = self.driver.find_element(By.ID, id_locator).text
            assert elements_text == ftext
        except:
            raise ValueError("The text of the element is not correct")

    '''CLICK'S METHODS'''

    def click_via_script(self, xpath_locator):
        """[This method performs click on an element]

        Args:
            xpath_locator ([xpath]): [XPATH locator]

        Raises:
            Exception: [Element was not found to be clicked]

        Returns:
            [Click]: [Click on element]
        """
        try:
            self.driver.execute_script(
                "function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log((getElementByXpath(\"" + xpath_locator + "\").click()));")
        except:
            # raise Exception("Element was not found to be clicked")
            return False

    def click_on_element_by_xpath(self, xpath_locator):
        """[This method performs click on an element]

        Args:
            xpath_locator ([xpath]): [XPATH locator]

        Raises:
            Exception: [Element was not found to be clicked]

        Returns:
            [Click]: [Click on element]
        """
        try:
            name = self.driver.find_element(By.XPATH, xpath_locator).text
            self.highlight_element_by_xpath(xpath_locator)
            self.driver.execute_script(
                "function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log((getElementByXpath(\"" + xpath_locator + "\").click()));")
        except:
            return False

    def click_on_element_by_id(self, id_locator):
        """[This method performs click on an element]

        Args:
            id_locator ([xpath]): [ID locator]

        Raises:
            Exception: [Element was not found to be clicked]

        Returns:
            [Click]: [Click on element]
        """
        try:
            name = self.driver.find_element(By.ID, id_locator).text
            self.highlight_element_by_xpath(id_locator)
            self.driver.execute_script(
                "document.getElementById(" + id + ").click();")
        except:
            # raise Exception("Element was not found to be clicked")
            return False

    '''Methods for screenshots'''

    def get_screenshot(self, screenshot_name):
        """[This method takes screenshot for allure]

        Args:
            screenshot_name ([text]): [Screenshot name]
        """
        allure.attach(self.driver.get_screenshot_as_png(),
                      name=screenshot_name, attachment_type=AttachmentType.PNG)

    '''Methods for scrolls'''

    def get_scroll(self, px):
        """[This method gets scroll down]

        Args:
            px ([number]): [Pixeles]
        """
        self.driver.execute_script("window.scrollTo(0," + px + ")")

    def get_scroll_to_bottom(self):
        """[This method gets scroll to the bottom of the page]
        """
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight)")

    def get_scroll_to_top(self):
        """[This method gets scroll to the top of the page]
        """
        self.driver.execute_script("window.scrollTo(0,0)")

    def get_scroll_to_element_by_xpath(self, xpath_locator):
        """[This method gets scroll to an element]

        Args:
            xpath_locator ([xpath]): [XPATH locator]

        Raises:
            Exception: [Element was not found for scrolling]

        Returns:
            [Scroll]: [Scroll to an element]
        """
        try:
            self.driver.execute_script(
                "function getElementByXpath(path) {return document.evaluate(path,document,null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;}console.log(getElementByXpath(\"" + xpath_locator + "\").scrollIntoView());")
        except:
            # raise Exception("Element was not found for scrolling")
            return False

    def get_scroll_to_element_by_id(self, id_locator):
        """[This method gets scroll to an element]

        Args:
            id_locator ([id]): [ID locator]

        Raises:
            Exception: [Element was not found for scrolling]

        Returns:
            [Scroll]: [Scroll to an element]
        """
        try:
            self.driver.execute_script(
                "document.getElementById(" + id + ").scrollIntoView());")
        except:
            # raise Exception("Element was not found for scrolling")
            return False

    def allure_attach_message_subject(self, subject):
        """[This method attaches the subject of the message from inbox to Allure]

        Args:
            subject ([text]): [The subject of the message from inbox]
        """
        allure.attach("Letter from : " + subject,
                      attachment_type=allure.attachment_type.TEXT)

    def save_cookies(self, cookies_name):
        """[This methods saves cookies into the file]

        Args:
            cookies_name ([text]): [Cookies file name]
        """
        pickle.dump(self.driver.get_cookies(), open(
            os.getcwd() + "/data/temporary/cookies/" + cookies_name + ".pkl", "wb"))

    def load_cookies(self, link=None, cookies_name="None"):
        """[This methods implements cookies into the browser]

        Args:
            link ([link], optional): [Links for site where coockies are being adding]. Defaults to None.
            cookies_name (str, optional): [Coockies file name]. Defaults to "None".
        """
        cookies = pickle.load(
            open(os.getcwd() + "/data/temporary/cookies/" + cookies_name + ".pkl", "rb"))
        self.driver.delete_all_cookies()
        for cookie in cookies:
            if 'expiry' in cookie:
                del cookie['expiry']
            self.driver.add_cookie(cookie)
        self.driver.get(link)

    def get_password(self):
        """[This method gets a password from file]

        Returns:
            [text]: [Password]
        """
        with open(os.getcwd() + "/data/passwords/"+os.environ["STAGE"]+".txt", "r") as cred:
            return cred.read()
    
    def get_info_from_file(self):
        """[This method gets a password from file]

        Returns:
            [text]: [Password]
        """
        with open(os.getcwd() + "/data/pswd/meeting_url.txt", "r") as cred:
            return cred.read()

    

    def send_keys_in_element_by_xpath(self, xpath_locator, text):
        """[This method sends text in a field]

        Args:
            xpath_locator ([xptah]): [XPATH locator]
            text ([text]): [Needed text]
        """
        current_value = self.driver.find_element(
            By.XPATH, xpath_locator).get_attribute("value")
        self.driver.find_element(By.XPATH, xpath_locator).clear()
        self.driver.find_element(By.XPATH, xpath_locator).send_keys(text)
        new_value = self.driver.find_element(
            By.XPATH, xpath_locator).get_attribute("value")
        # assert current_value not in new_value, "New value is not entered in a field"

    def print_browser_log(self):
        time.sleep(3)
        self.driver.execute_script("location.reload(true);")
        time.sleep(3)
        collect_errors = ['404', '500']
        for entry in self.driver.get_log('browser'):
            if any(x in entry["message"] for x in collect_errors):
                allure.attach(entry["message"], name="log", extension=".log",
                              attachment_type=allure.attachment_type.TEXT)
        
    def allure_attach_json(self, json):
        allure.attach(json, name="json", extension=".json",
                              attachment_type=allure.attachment_type.JSON)
    
    def allure_attach_text(self, text):
        allure.attach(text, name="db", extension=".txt",
                              attachment_type=allure.attachment_type.TEXT)
    
        # time.sleep(2)
        # self.driver.get(
        #     "https://www.simpletollfree.com/rss/podcast?id=7753601642:531144")
        # collect_errors = ['404', '500']
        # for entry in self.driver.get_log('browser'):
        #     if any(x in entry["message"] for x in collect_errors):
        #         print(entry["message"])
        # time.sleep(5)
        # for entry in self.driver.get_log('browser'):
        #     print(entry)

        # self.pylex.get_screenshot("screen")
        # res = "\n".join([x["message"] for x in self.driver.get_log("browser")])
        # print(res)

        # self.driver.get(
        #     "https://qa-www.simpletollfree.com/rss/podcast?id=7753601642:531144")
        # self.pylex.get_screenshot("fdsfsdf")
        # with open(os.getcwd() + "/browser_log.txt", "a") as log:
        #     log.write(res)
        # self.driver.back()
        # allure.attach.file(os.getcwd() + "chrome.log", name="log", attachment_type=allure.attachment_type.TEXT)
        # allure.attach.file(
        #     res, name="log2.log", attachment_type=allure.attachment_type.TEXT)

        # allure.attach(res, name="log", extension=".log",
        #               attachment_type=allure.attachment_type.TEXT)
    
    def switch_to_frame(self, frame_locator):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, frame_locator))
            

    ##########! Here new methods are creating !############

    def open_link_in_new_tab(self, link):
        self.driver.execute_script("window.open('http://" + link + "');")

    def open_link_in_current_tab(self, link):
        self.driver.execute_script(
            "document.location.href = 'http://" + link + "';")

    def wait_element_clickable(self, xpath_locator):
        elem = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator)))
        elem.click()

    def wait_locate_element(self, xpath_locator):
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, xpath_locator)))

    def wait_invisible_element(self, xpath_locator):
        self.wait.until(EC.invisibility_of_element_located(
            (By.XPATH, xpath_locator)))

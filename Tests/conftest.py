import pytest
import os
import time
from config import Config
# from dateutil.relativedelta import *
# import cx_Oracle
# from typing import Coroutine
# from dateutil.relativedelta import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

pytest_plugins = []
ENVSTACK_URL = 'https://akoledachkin1:LSk49C5EzMBrxNX5Rvqy@hub-cloud.browserstack.com/wd/hub'
BUILD_PATH = 'build'

# Creating of ignore list. It will be used in the future for running tests independens
collect_ignore = [
    'projects/api_only',
    'projects/common',
    'projects/integration',
    'projects/mobile',
    'projects/hyperskill'
]

# Dependenses for projects (it tells what will be runned)
if os.environ['STAGE'].startswith('api_only'):
    collect_ignore.remove('projects/api_only')
    print(os.environ['STAGE'])

elif os.environ['STAGE'].startswith('combase1') or os.environ['STAGE'].startswith('combase2'):
    collect_ignore.remove('projects/common')
    print(os.environ['STAGE'])

elif os.environ['STAGE'].startswith('integration'):
    collect_ignore.remove('projects/integration')
    print(os.environ['STAGE'])

elif os.environ['STAGE'].startswith('mobile'):
    collect_ignore.remove('projects/mobile')
    print(os.environ['STAGE'])

elif os.environ['STAGE'].startswith('hyperskill'):
    collect_ignore.remove('projects/hyperskill')
    print(os.environ['STAGE'])


# elif os.environ['STAGE'].startswith('common_base1') or os.environ['STAGE'].startswith('common_base2'):
#     collect_ignore.remove('projects/common')
#     print(os.environ['STAGE'])




@pytest.fixture(scope="function")
def get_options():
    if os.environ["ENV"] == "chrome_pc":
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": os.getcwd() + "/downloads",
            "safebrowsing.enabled": "false"
        }
        options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-impl-side-painting')
        options.add_argument('--disable-gpu-sandbox')
        options.add_argument('--disable-accelerated-2d-canvas')
        options.add_argument('--disable-accelerated-jpeg-decoding')
        options.add_argument('--test-type=ui')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument(
            "--use-file-for-fake-audio-capture="+os.getcwd()+"/src/small_music.mp3")
        options.add_experimental_option("prefs", preferences)
        return options

    elif os.environ["ENV"] == "chrome":
        options = webdriver.ChromeOptions()
        preferences = {
            "download.default_directory": os.getcwd() + "/downloads",
            "safebrowsing.enabled": "false"
        }
        options.add_argument('--no-sandbox')
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-impl-side-painting')
        options.add_argument('--disable-gpu-sandbox')
        options.add_argument('--disable-accelerated-2d-canvas')
        options.add_argument('--disable-accelerated-jpeg-decoding')
        options.add_argument('--test-type=ui')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--use-fake-ui-for-media-stream")
        options.add_argument(
            "--use-file-for-fake-audio-capture=/src/small_music.mp3")
        options.add_experimental_option("prefs", preferences)
        return options

    elif os.environ["ENV"] == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-impl-side-painting')
        options.add_argument('--disable-gpu-sandbox')
        options.add_argument('--disable-accelerated-2d-canvas')
        options.add_argument('--disable-accelerated-jpeg-decoding')
        options.add_argument('--test-type=ui')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--use-fake-device-for-media-stream")
        options.add_argument("--use-fake-ui-for-media-stream")
        # options.add_argument("--ENV.download.manager.showWhenStarting", False)
        # options.add_argument("--ENV.download.dir", os.getcwd() + "/downloads")
        # options.add_argument("--ENV.helperApps.neverAsk.saveToDisk", "text/csv/mp3/pdf")
        # options.add_argument("dom.disable_beforeunload", True)
        # options.add_argument(
        #     "--use-file-for-fake-audio-capture=/src/small_music.mp3")
        return options
    
    elif os.environ["ENV"] == "brstack":
        desired_cap = {
            "os" : "OS X",
            "os_version" : "Big Sur",
            "ENV" : "Safari",
            "ENV_version" : "14.0",
            "resolution" : "1920x1080",
            "ENVstack.local" : "false",
            "ENVstack.selenium_version" : "3.14.0",
            'verify_ssl' : False
        }
        return desired_cap
    
    elif os.environ["ENV"] == "android":
        from appium.webdriver.appium_service import AppiumService
        appium_service = AppiumService()
        desired_caps = {
            "platformName": "Android",
            "appium:platformVersion": "11.0",
            "appium:deviceName": "Android Emulator",
            "appium:app": os.getcwd() + "/app_binaries/android/" + Config.config[os.environ['STAGE']]['APP'] + ".apk",
            "appium:udid": "emulator-5554",
            "appium:autoGrantPermission": True,
            # "appium:appWaitActivity": "*",
            "appium:appPackage": "app." + Config.config[os.environ['STAGE']]['APP'] + ".app",
            "appium:appActivity": "com.carrierx.meetingclient.ui.activities.LaunchActivity"
        }
        return desired_caps


@pytest.fixture(scope="function", autouse=True)
def driver(request, get_options):
    if os.environ["ENV"] == "chrome_pc":
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.quit()
    
    elif os.environ["ENV"] == "chrome":
        driver = webdriver.Chrome(options=get_options)
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.quit()

    elif os.environ["ENV"] == "firefox":
        driver = webdriver.Firefox(options=get_options, executable_path="geckodriver")
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.close()
    
    elif os.environ["ENV"] == "safari":
        driver = webdriver.Safari()
        request.cls.driver = driver
        yield
        driver.delete_all_cookies()
        driver.close()
    
    elif os.environ["ENV"] == "brstack":
        driver = webdriver.Remote(
            command_executor=ENVSTACK_URL,
            desired_capabilities=get_options
        )
        request.cls.driver = driver
        yield
        driver.close()

    elif os.environ["ENV"] == "android":
        if appium_service.start():
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", get_options)
            request.cls.driver = driver
            yield
            appium_service.stop()
        else:
            pass

    elif os.environ["ENV"] is None:
        pass


# def db_connect():





# cx_Oracle.init_oracle_client(lib_dir="/usr/lib/oracle/19.13/client64/lib")
# dsn_tns = cx_Oracle.makedsn('lb-qadb.int', '1521', service_name='fcc')
# connection = cx_Oracle.connect(user=r'FCCUSER', password='fccuser', dsn=dsn_tns)


# @pytest.fixture(scope="function")
# def connection():
#     dsn = cx_Oracle.makedsn(
#             'lgb3-db.int', 
#             '1522', 
#             service_name='fcc'
#         )
#     connection = cx_Oracle.connect(
#         user='FCCUSER', 
#         password='fccuser', 
#         dsn=dsn
#     )
#     return connection
# connection = connection()

# @pytest.fixture(scope="function")
# def connect(connection):
#     cursor = connection.cursor()
#     return cursor


# @pytest.fixture(scope="function")
# def close_connection(connection):
#     connection.close()

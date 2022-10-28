

from email import header
import pytest
import requests
import os
# from dateutil.relativedelta import *
from config import Config
from requests.auth import HTTPBasicAuth



class ApiRequest:

    #* Create a new session for each test
    def __enter__(self):
        # self.server = Config.config[os.environ['STAGE']]['SERVER']
        # self.server = None
        # self.auth = HTTPBasicAuth(
        #     Config.config[os.environ['STAGE']]['API_LOGIN'], Config.config[os.environ['STAGE']]['API_PASSWORD'])
        self.session = requests.Session()
        return self
        

    def __exit__(self, a, b, c):
        pass

    def get_cat_fact(self):
        response = self.session.get("https://catfact.ninja/fact",
        headers={
                "Content-Type": "application/json",
                "Service-Id": "462"  
            },
            verify=False
        )

        r = response.json()
        assert response.ok
        return r['fact']
        print(str(r['fact']))

    
import os
from config import Config

class Data:

	ACCOUNT_LOGIN = Config.config[os.environ['STAGE']]['ACCOUNT_LOGIN']
	ACCOUNT_PASSWORD = Config.config[os.environ['STAGE']]['ACCOUNT_PASSWORD']
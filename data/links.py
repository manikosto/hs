import os
from config import Config

class Links:
    if os.environ["STAGE"] == "hyperskill-release-tests":
        prefix = "https://release:512@" + str(Config.config[os.environ['STAGE']]['DOMAIN'])
        tasks = {
            "theory": prefix + str(Config.links[os.environ['STAGE']]['THEORY_TASK'])
        }
    elif os.environ["STAGE"] == "hyperskill-prod-tests":
        prefix = str(Config.config[os.environ['STAGE']]['DOMAIN'])
    
    tracks_page = prefix + str(Config.links[os.environ['STAGE']]['TRACKS_PAGE'])
    login_page = prefix + str(Config.links[os.environ['STAGE']]['LOGIN_PAGE'])
    
    
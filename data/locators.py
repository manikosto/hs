import os


class Locators:

    if os.environ["STAGE"] == "hyperskill-prod-tests":
        pass
    elif os.environ["STAGE"] == "hyperskill-release-tests":
        pass

    # Tasks
    NEXT_SECTION_BUTTON = "//button[@click-event-target='next_section']"
    EXPAND_ALL_LINK = "//a[@click-event-target='expand_all']"
    START_PRACTICING_BUTTON = "//button[@click-event-target='start_practicing']"
    VERIFY_TO_SKIP_BUTTON = "(//button[text()=' Verify to skip '])[1]"
    SECTION_COUNTER = "//span[contains(@class, 'text-secondary')]"
    
    HOME_TITLE = "Tracks – JetBrains Academy — Learn programming by building your own apps"
    LOGO = "(//a[@href='/tracks'])[1]"
    CARD = "(//div[contains(@class, 'card')])[9]"
    EMAIL_FIELD = "//input[@type='email']"
    PASSWORD_FIELD = "//input[@type='password']"
    SUBMIT_BUTTON = "//button[@type='submit']"


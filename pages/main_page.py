import logging
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_to_login_page(self):
        logging.info("Going to login")
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        logging.info("Checking availability of login link")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

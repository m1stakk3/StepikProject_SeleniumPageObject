import logging
from pages.main_page import MainPage
from pages.locators import LoginPageLocators


class LoginPage(MainPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        logging.info("Checking current url of login page")
        assert self.browser.current_url() == "http://selenium1py.pythonanywhere.com/accounts/login/", "Not expected URL"

    def should_be_login_form(self):
        logging.info("Checking logging form")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Did not find login form"

    def should_be_register_form(self):
        logging.info("Checking registry form")
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Did not find register form"

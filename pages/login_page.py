import logging
from pages.main_page import MainPage
from pages.locators import LoginPageLocators
from selenium.common.exceptions import NoSuchElementException


class LoginPage(MainPage):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def should_be_login_page(self) -> None:
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) -> None:
        logging.info("Checking current url of login page")
        assert self.browser.current_url() == "http://selenium1py.pythonanywhere.com/accounts/login/", "Not expected URL"

    def should_be_login_form(self) -> None:
        logging.info("Checking logging form")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Did not find login form"

    def should_be_register_form(self) -> None:
        logging.info("Checking registry form")
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Did not find register form"

    def register_new_user(self, email: str, password: str) -> None:
        self.go_to_login_page()
        self.should_be_login_form()
        self.should_be_register_form()

        for locator in [LoginPageLocators.REGISTER_EMAIL_FORM, LoginPageLocators.REGISTER_PASSWORD_FORM,
                        LoginPageLocators.REGISTER_PASSWORD_REENTER_FORM, LoginPageLocators.REGISTER_BUTTON]:
            if not self.is_element_present(*locator):
                raise NoSuchElementException

        # обозначение полей
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_FORM)
        password_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_FORM)
        password_reenter_form = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REENTER_FORM)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        # действия с полями
        logging.info("Entering user data")
        input_data = zip([email_form, password_form, password_reenter_form], [email, password, password])
        for form, data in input_data:
            while len(form.get_attribute('value')) != len(data):
                form.clear()
                form.send_keys(data)
        register_button.click()

        # проверка входа пользователя
        self.should_be_authorized_user()

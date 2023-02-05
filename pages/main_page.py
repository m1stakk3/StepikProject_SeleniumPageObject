from pages.base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        basket_button.click()

    def save_item_name(self):
        item_name = self.browser.find_element(*MainPageLocators.ITEM_NAME).text
        return item_name

    def check_item_added_to_basket(self, item_name):
        info = self.browser.find_element(*MainPageLocators.ITEM_IN_BASKET).text
        assert info == item_name, "Item wasn't added to basket"

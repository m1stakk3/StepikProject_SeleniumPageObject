from pages.base_page import BasePage
from pages.locators import MainPageLocators, ItemPageLocators, AfterAddToBasketPageLocators


class MainPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"


class ItemPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ItemPageLocators.BASKET_BUTTON)
        basket_button.click()

    def save_item_name(self):
        item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
        return item_name

    def save_item_price(self):
        price = self.browser.find_element(*ItemPageLocators.PRICE).text
        return price

    def check_item_added_to_basket(self, item_name):
        info = self.browser.find_element(*AfterAddToBasketPageLocators.ITEM_NAME).text
        assert info == item_name, "Item wasn't added to basket"

    def check_item_price_in_basket(self, item_price):
        info = self.browser.find_element(*AfterAddToBasketPageLocators.PRICE).text
        assert info == item_price, "Item price in basket not equals before addition"

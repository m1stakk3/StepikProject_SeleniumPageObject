import logging
from typing import Union
from pages.main_page import MainPage
from pages.locators import ItemPageLocators, BasketPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

StrNone = Union[str, None]


class ItemPage(MainPage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.item_name: StrNone = None
        self.item_price: StrNone = None

    def add_to_basket(self):
        logging.info("Trying to add to basket")
        self.browser.find_element(*ItemPageLocators.BASKET_BUTTON).click()

    def save_item_name(self):
        logging.info("Getting item name")
        self.item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
        logging.info("Item name: {}".format(self.item_name))

    def save_item_price(self):
        logging.info("Getting item price")
        self.item_price = self.browser.find_element(*ItemPageLocators.PRICE).text
        logging.info("Item price: {}".format(self.item_price))

    def check_item_added_to_basket(self):
        try:
            WebDriverWait(driver=self.browser, timeout=15).until(
                EC.text_to_be_present_in_element(locator=BasketPageLocators.ITEM_NAME, text_=self.item_name),
            )
        except TimeoutException:
            assert False, "Item wasn't add to basket"

    def check_item_price_in_basket(self):
        try:
            WebDriverWait(driver=self.browser, timeout=15).until(
                EC.text_to_be_present_in_element(locator=BasketPageLocators.ITEM_PRICE, text_=self.item_price),
            )
        except TimeoutException:
            assert False, "Item wasn't add to basket"

        info = self.browser.find_element(*BasketPageLocators.ITEM_PRICE).text
        assert info == self.item_price, "Item price in basket not equals before addition"

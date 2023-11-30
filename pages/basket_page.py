from pages.locators import BasketPageLocators
from pages.main_page import BasePage


class BasketPage(BasePage):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def is_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Expected message"

    def is_basket_empty(self):
        assert self.is_not_element_present(BasketPageLocators.BASKET_ITEMS_CONTAINER), "Expected no items"

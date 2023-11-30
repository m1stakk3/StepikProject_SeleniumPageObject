from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class BasePageLocators:
    LOGIN_LINK: tuple = (By.XPATH, '//a[@id="login_link"]')
    BASKET_BUTTON: tuple = (By.XPATH, '//a[@class="btn btn-default"]')


@dataclass
class MainPageLocators(BasePageLocators):
    pass


@dataclass
class LoginPageLocators(MainPageLocators):
    LOGIN_FORM: tuple = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM: tuple = (By.XPATH, '//form[@id="register_form"]')


@dataclass
class ItemPageLocators(MainPageLocators):
    BASKET_BUTTON: tuple = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    ITEM_NAME: tuple = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRICE: tuple = (By.XPATH, '//p[@class="price_color"]')
    SUCCESS_MESSAGE: tuple = (By.XPATH, '//*[@class="alert alert-safe alert-noicon alert-success  fade in"][1]')


@dataclass
class BasketPageLocators:
    ITEM_NAME: tuple = (By.XPATH, '//*[@class="col-sm-4"]/h3/a')
    ITEM_PRICE: tuple = (By.XPATH, '//*[@class="col-sm-1"]/*[@class="price_color align-right"]')
    ITEM_TOTAL_PRICE: tuple = (By.XPATH, '//*[@class="col-sm-2"]/*[@class="price_color align-right"]')
    EMPTY_MESSAGE: tuple = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_ITEMS_CONTAINER: tuple = (By.XPATH, '//*[@class="basket-items"]')

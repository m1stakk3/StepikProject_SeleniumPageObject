from selenium.webdriver.common.by import By
from dataclasses import dataclass


@dataclass
class MainPageLocators:
    LOGIN_LINK: tuple = (By.XPATH, '//a[@id="login_link"]')


@dataclass
class LoginPageLocators(MainPageLocators):
    LOGIN_FORM: tuple = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM: tuple = (By.XPATH, '//form[@id="register_form"]')


@dataclass
class ItemPageLocators:
    BASKET_BUTTON: tuple = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    ITEM_NAME: tuple = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRICE: tuple = (By.XPATH, '//p[@class="price_color"]')


@dataclass
class BasketPageLocators:
    ITEM_NAME: tuple = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ITEM_PRICE: tuple = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")


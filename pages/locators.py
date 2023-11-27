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
    BASKET_BUTTON: tuple = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME: tuple = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE: tuple = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')


class AfterAddToBasketPageLocators:
    ITEM_NAME: tuple = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE: tuple = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")


from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class ItemPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')


class AfterAddToBasketPageLocators:
    ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")

from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")

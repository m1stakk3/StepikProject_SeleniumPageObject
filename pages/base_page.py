import math
import logging
from pages.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        logging.info("Creating browser exemplar")
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        logging.info("Getting url: {}".format(self.url))
        self.browser.get(self.url)

    def go_to_basket(self):
        logging.info("Going to basket")
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    def is_element_present(self, how, what):
        logging.info("Trying to check presence of element")
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logging.error(NoSuchElementException)
            return False
        logging.info("Element is present!")
        return True

    def is_not_element_present(self, locator, timeout=4):
        logging.info("Trying to check not presence of element")
        try:
            Wait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        logging.info("Element is not present!")
        return False

    def is_disappeared(self, locator, timeout=4):
        logging.info("Trying to check that element is disappeared")
        try:
            Wait(self.browser, timeout, 1, [TimeoutException]).until_not(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        logging.info("Element is disappeared")
        return True

    def solve_quiz_and_get_code(self):
        logging.info("Solving quiz...")
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            logging.info(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            logging.info("No second alert presented [Good]")
        else:
            logging.error("Some unexpected alert!")

import math
import logging
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        logging.info("Creating browser exemplar")
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        logging.info("Getting url: {}".format(self.url))
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        logging.info("Trying to check presence of element")
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            logging.error(NoSuchElementException)
            return False
        logging.info("Element is present!")
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

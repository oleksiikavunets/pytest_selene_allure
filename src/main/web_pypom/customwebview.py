from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class CustomWebView:

    def find_element_with_wait(self, driver, timeout, by, locator,
                               ignored_exceptions=(StaleElementReferenceException, NoSuchElementException,)):
        return WebDriverWait(driver,
                             timeout,
                             ignored_exceptions=ignored_exceptions).until(
            expected_conditions.presence_of_element_located((by, locator)))

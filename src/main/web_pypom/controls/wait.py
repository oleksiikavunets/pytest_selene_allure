from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def wait(action):
    def decor(self):
        WebDriverWait(self.driver, 30).until(ec.visibility_of_element_located(locator=self.locator))
        action(self)
        return
    return decor


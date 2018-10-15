from src.main.web_pypom.controls.base_control import BaseControl
from selenium.webdriver.common.by import By
from src.main.web_pypom.controls.wait import wait
from time import sleep


class Button(BaseControl):
    def __init__(self, driver, locator='//*[@id="tsf"]/div[2]/div[3]/center/input[2]'):
        self.locator = (By.XPATH, locator)
        self.driver = driver

    @property
    def button(self):
        return self.driver.find_element(*self.locator)

    @property
    @wait
    def click(self):
        return self.button.click()


if __name__ == '__main__':
    from selenium.webdriver import Chrome
    driver = Chrome()
    driver.get('https://www.google.com')
    bc = Button(driver)
    bc.click
    sleep(3)
    driver.quit()

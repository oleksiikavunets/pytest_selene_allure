import pytest
import allure
from allure_commons.types import AttachmentType

from selene import config, browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def setup():
    config.browser_name = 'chrome'
    config.reports_folder = 'reports'
    config.base_url = "https://www.wikipedia.org"

    options = Options()
    options.add_argument("--start-maximized")
    desired_capabilities = {'browserName': 'chromium',
                            'version': '2.38',
                            'javascriptEnabled': True}

    desired_capabilities1 = options.to_capabilities()
    desired_capabilities1.update(desired_capabilities)
    driver = webdriver.Remote(
        command_executor='http://192.168.152.128:9515',
        desired_capabilities=desired_capabilities1
    )
    browser.set_driver(driver)
    yield
    teardown()


def teardown():
    browser.quit()


def pytest_exception_interact(node, call, report):
    print("\nTEST FAILED IN !!!!!!!!!!!!!!!!")
    print("CALL: " + str(call))
    attach = browser.driver().get_screenshot_as_png()
    allure.attach(attach, name="Screenshot", attachment_type=AttachmentType.PNG)

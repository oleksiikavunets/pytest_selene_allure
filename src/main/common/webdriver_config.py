from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from src.main.common.base_config import REMOTE_RUN, REMOTE_HOST, REMOTE_PORT, BASE_URL
from selene import config, browser


def configure_driver():
    config.browser_name = 'chrome'
    config.reports_folder = 'reports'
    config.base_url = BASE_URL

    if REMOTE_RUN:
        _configure_remote_driver()


def _configure_remote_driver():
    options = Options()
    options.add_argument("--start-maximized")
    caps = {'browserName': 'chromium',
            'version': '2.38',
            'javascriptEnabled': True}

    desired_capabilities = options.to_capabilities()
    desired_capabilities.update(caps)

    driver = webdriver.Remote(
        command_executor=REMOTE_HOST + ":" + REMOTE_PORT,
        desired_capabilities=desired_capabilities
    )

    browser.set_driver(driver)

import allure
import pytest
from allure_commons.types import AttachmentType
from selene import browser

from src.main.common.base_config import bc
from src.main.common.rerun_controller import rerun_controller
from src.main.common.webdriver_config import configure_driver


@pytest.fixture(scope="session")
def setup(request):
    if not bc.test_session_started:
        print("\n>>> Before Session")
        bc.set_test_session_started()
        configure_driver()
        rerun_controller.add_test_to_listener(request.node.items[-1])

    yield
    if rerun_controller.are_reruns_out():
        bc.set_test_session_closed()
    browser.quit()
    print("\n>>> After Session\n")
    print("CLOSING SSH CONNECTION\n")


@pytest.fixture(scope="class")
def setup_class():
    print("\n      >>> Before Class")

    yield
    print("\n      >>> After Class")


@pytest.fixture(scope="function")
def setup_function(request):
    print("\n         >>> Before Function")

    if rerun_controller.is_test_listened(request.node.name):
        rerun_controller.add_rerun()

    yield
    print("\n         >>> After Function")


def pytest_exception_interact(node, call, report):
    print("\nTEST FAILED IN !!!!!!!!!!!!!!!!")
    attach = browser.driver().get_screenshot_as_png()
    allure.attach(attach, name="Screenshot", attachment_type=AttachmentType.PNG)

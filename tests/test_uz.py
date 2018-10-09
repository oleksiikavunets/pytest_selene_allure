import pytest
from flaky import flaky
from selene import config, browser
from time import sleep
from src.main.common.base_config import MAX_RUN
from src.main.new_job.screens.search_screen import SearchScreen


@flaky(max_runs=MAX_RUN)
@pytest.mark.usefixtures("setup_class", "setup_function")
class TestUz:

    def test_can_open_uz(self):
        SearchScreen.open()
        assert browser.title() == 'Online reservation and purchase tickets - Ukrzaliznytsia'

    def test_can_login(self):
        SearchScreen.open()
        searchScreen = SearchScreen()
        searchScreen.authorizeForm.click()
        searchScreen.authorizeForm.activateAuthorizeButton.click()
        searchScreen.authorizeForm.emailField.send_keys('qavunets@gmail.com')
        searchScreen.authorizeForm.passwordField.send_keys('qavunets@gmail.com')
        searchScreen.authorizeForm.authorizeButton.click()


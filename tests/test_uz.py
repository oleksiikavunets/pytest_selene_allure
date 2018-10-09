import pytest
from flaky import flaky
from selene import config, browser
from time import sleep

from selene.support.conditions import have

from src.main.common.base_config import MAX_RUN, EMAIL, PASSWORD
from src.main.new_job.screens.search_screen import SearchScreen
from selenium.webdriver.support import  expected_conditions as ec


@flaky(max_runs=MAX_RUN)
@pytest.mark.usefixtures("setup_class", "setup_function")
class TestUz:

    def test_can_open_uz(self):
        SearchScreen.open()
        assert browser.title() == 'Online reservation and purchase tickets - Ukrzaliznytsia'

    def test_can_login(self):
        SearchScreen.open()
        searchScreen = SearchScreen()
        authorizeForm = searchScreen.authorizeForm

        btnNameBefore = authorizeForm.activateAuthorizeButton.text

        authorizeForm.activateAuthorizeButton.click()
        authorizeForm.emailField.send_keys(EMAIL)
        authorizeForm.passwordField.send_keys(PASSWORD)
        authorizeForm.authorizeButton.click()
        authorizeForm.activateAuthorizeButton.should_not(have.text(btnNameBefore))

        btnNameAfter = authorizeForm.activateAuthorizeButton.text
        assert btnNameAfter == EMAIL.split("@")[0]

    def test_can_not_login(self):
        SearchScreen.open()
        searchScreen = SearchScreen()
        authorizeForm = searchScreen.authorizeForm

        btnNameBefore = authorizeForm.activateAuthorizeButton.text

        authorizeForm.activateAuthorizeButton.click()
        authorizeForm.emailField.send_keys(EMAIL)
        authorizeForm.passwordField.send_keys("wertyui")
        authorizeForm.authorizeButton.click()
        authorizeForm.activateAuthorizeButton.should_not(have.text(btnNameBefore))

        btnNameAfter = authorizeForm.activateAuthorizeButton.text
        assert btnNameAfter == EMAIL.split("@")[0]


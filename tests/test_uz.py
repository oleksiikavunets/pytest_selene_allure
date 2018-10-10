import time

import pytest
from flaky import flaky
from selene import browser
from selene.support.conditions import be

from src.main.common.base_config import MAX_RUN, EMAIL
from src.main.new_job.screens.search_screen import SearchScreen
from tests.utils.asserts import Assert
from tests.utils.data_provider import DataProvider


@flaky(max_runs=MAX_RUN)
@pytest.mark.usefixtures("setup_class", "setup_function")
class TestUz:

    def test_can_open_uz(self):
        SearchScreen.open()
        assert browser.title() == 'Online reservation and purchase tickets - Ukrzaliznytsia'

    @pytest.mark.parametrize('is_passed, email, password',
                             DataProvider.loadData(__file__, "test_can_login"))
    def test_can_login(self, is_passed, email, password):
        SearchScreen.open()
        searchScreen = SearchScreen()
        authorizeForm = searchScreen.authorizeForm

        btnNameBefore = authorizeForm.activateAuthorizeButton.text

        authorizeForm.activateAuthorizeButton.click()
        authorizeForm.emailField.send_keys(email)
        authorizeForm.passwordField.send_keys(password)
        authorizeForm.authorizeButton.click()
        # wait method for changes here
        time.sleep(5)
        # if is_passed:
        #     authorizeForm.activateAuthorizeButton.should_not(have.text(btnNameBefore))
        # else:
        #     authorizeForm.activateAuthorizeButton.should(have.text(btnNameBefore))
        btnNameAfter = authorizeForm.activateAuthorizeButton.text
        Assert.assert_with_condition(btnNameAfter == EMAIL.split("@")[0], is_passed,
                                     message=f"Email={email} and password={password}")

    def test_logo_is_displayed(self):
        SearchScreen.open()
        SearchScreen().logoButton.should(be.visible)

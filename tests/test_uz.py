import time
import allure
import pytest
from flaky import flaky
from selene import browser

from src.main.common.base_config import MAX_RUN
# from src.main.web.screens.search_screen import SearchScreen - without PyPOM
from src.main.web_pypom.searchscreen import SearchScreen
from tests.utils.asserts import Assert
from tests.utils.data_provider import DataProvider


@allure.feature('Ukrzaliznytsia Booking main page')
@flaky(max_runs=MAX_RUN)
@pytest.mark.usefixtures("setup_class", "setup_function")
class TestUz:
    @allure.title('Page title verification')
    @allure.severity(allure.severity_level.NORMAL)
    def test_can_open_uz(self):
        SearchScreen().open()
        assert browser.title() == 'Online reservation and purchase tickets - Ukrzaliznytsia'

    @allure.title('Logo visibility verification')
    @allure.severity(allure.severity_level.NORMAL)
    def test_logo_is_displayed(self):
        assert SearchScreen().open().logo_button.is_displayed() is True

    @allure.title('User authorization')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('is_passed, email, password',
                             DataProvider.loadData(__file__, "test_can_login"))
    def test_can_login(self, is_passed, email, password):
        search_screen = SearchScreen().open()
        authorize_form = search_screen.authorize_form
        authorize_form.auth_form_activate.click()
        authorize_form.email_field.send_keys(email)
        authorize_form.pwd_field.send_keys(password)
        authorize_form.enter_button.click()
        # wait method for changes here
        time.sleep(1)
        btn_name_after = authorize_form.auth_form_activate.text
        Assert.assert_with_condition(btn_name_after == email.split("@")[0], is_passed,
                                     message=f"Email={email} and password={password}")

    # Without PyPOM
    # @allure.title('Page title verification')
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_can_open_uz(self):
    #     SearchScreen.open()
    #     assert browser.title() == 'Online reservation and purchase tickets - Ukrzaliznytsia'
    #
    # @allure.title('Logo visibility verification')
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_logo_is_displayed(self):
    #     SearchScreen.open()
    #     SearchScreen().logoButton.should(be.visible)
    #
    # @allure.title('User authorization')
    # @allure.severity(allure.severity_level.CRITICAL)
    # @pytest.mark.parametrize('is_passed, email, password',
    #                          DataProvider.loadData(__file__, "test_can_login"))
    # def test_can_login(self, is_passed, email, password):
    #     SearchScreen.open()
    #     search_screen = SearchScreen()
    #     authorize_form = search_screen.authorizeForm
    #     authorize_form.activateAuthorizeButton.click()
    #     authorize_form.emailField.send_keys(email)
    #     authorize_form.passwordField.send_keys(password)
    #     authorize_form.authorizeButton.click()
    #     # wait method for changes here
    #     time.sleep(1)
    #     btn_name_after = authorize_form.activateAuthorizeButton.text
    #     Assert.assert_with_condition(btn_name_after == email.split("@")[0], is_passed,
    #                                  message=f"Email={email} and password={password}")

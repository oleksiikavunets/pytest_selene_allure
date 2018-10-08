import pytest
import allure
from src.main.forsampletest.pages.SearchPage import SearchPage
from tests.utils.data_provider import DataProvider


@allure.feature('Wikipedia Search')
@pytest.mark.usefixtures("setup")
class TestSample:

    @allure.title('Search text on Wikipedia')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase('https://servicedesk.luxoft.com/browse/SD-1261407', 'Headset request')
    @pytest.mark.parametrize('is_passed, search, expected', DataProvider.loadData1("sample"))
    def test_aaa(self, is_passed, search, expected):
        search_page = SearchPage()
        search_page.open()
        article_page = search_page.search(search)
        if is_passed:
            assert article_page.heading.text == expected
        else:
            assert article_page.heading.text != expected

    # def test_function(self):
    #     assert True is not True

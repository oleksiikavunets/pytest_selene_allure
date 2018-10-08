from selene.support.jquery_style_selectors import s
from selene import browser

from src.main.forsampletest.elements.Button import Button
from src.main.forsampletest.pages.ArticlePage import ArticlePage
import allure


class SearchPage:
    def __init__(self):
        self.searchInput = s('#searchInput')
        self.searchBtn = Button('[type="submit"]')

    @allure.step("Open page")
    def open(self):
        browser.open_url("/")
        return self

    @allure.step("Search {1}")
    def search(self, search):
        self.searchInput.set(search)
        self.searchBtn.click()
        return ArticlePage()

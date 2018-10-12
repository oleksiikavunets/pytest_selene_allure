from pypom import Page, Region
from selene import browser
from src.main.web_pypom.customwebview import CustomWebView
from selenium.webdriver.common.by import By


class SearchScreen(Page, CustomWebView):
    BASE_URL = 'https://booking.uz.gov.ua/en/'
    URL_TEMPLATE = '/'

    def __init__(self, timeout=10, **url_kwargs):
        super(SearchScreen, self).__init__(browser.driver(), self.BASE_URL, timeout, **url_kwargs)

    @property
    def logo_button(self):
        return self.find_element_with_wait(self.driver, self.timeout, By.CSS_SELECTOR,
                                           'body > div.b-page-header > div > div.top-row > a.uz-logo')

    @property
    def main_form(self):
        root = self.find_element_with_wait(self.driver, self.timeout, By.XPATH, '//*[@id="search-frm"]/form')
        return self.MainForm(self, root=root)

    @property
    def authorize_form(self):
        root = self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                           '/html/body/div[1]/div/div[3]/div[6]/div')
        return self.AuthorizeForm(self, root=root)

    class MainForm(Region, CustomWebView):

        @property
        def from_field(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '//*[@id="search-frm"]/form/div[2]/div[1]/div[1]/input')

        @property
        def to_field(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '//*[@id="search-frm"]/form/div[2]/div[1]/div[2]/input')

        @property
        def search_button(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '//*[@id="search-frm"]/form/div[3]/div/button')

    class AuthorizeForm(Region, CustomWebView):

        @property
        def auth_form_activate(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '/html/body/div[1]/div/div[3]/div[6]/a')

        @property
        def email_field(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '/html/body/div[1]/div/div[3]/div[6]/div/form/input')

        @property
        def pwd_field(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '/html/body/div[1]/div/div[3]/div[6]/div/form/div[2]/input')

        @property
        def enter_button(self):
            return self.find_element_with_wait(self.driver, self.timeout, By.XPATH,
                                               '/html/body/div[1]/div/div[3]/div[6]/div/form/div[4]/button')



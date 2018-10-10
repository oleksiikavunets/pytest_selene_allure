from pypom import Page, Region
from selenium.webdriver.common.by import By


class SearchScreen(Page):
    @property
    def main_form(self):
        root = self.find_element(By.XPATH, '//*[@id="search-frm"]/form')
        return MainForm(self, root=root)

    @property
    def authorize_form(self):
        root = self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[6]/div')
        return AuthorizeForm(self, root=root)


class MainForm(Region):
    @property
    def from_field(self):
        return self.find_element(By.XPATH, '//*[@id="search-frm"]/form/div[2]/div[1]/div[1]/input')

    @property
    def to_field(self):
        return self.find_element(By.XPATH, '//*[@id="search-frm"]/form/div[2]/div[1]/div[2]/input')

    @property
    def search_button(self):
        return self.find_element(By.XPATH, '//*[@id="search-frm"]/form/div[3]/div/button')


class AuthorizeForm(Region):

    @property
    def auth_form_activate(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[6]/a')

    @property
    def email_field(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[6]/div/form/input')

    @property
    def pwd_field(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[6]/div/form/div[2]/input')

    @property
    def enter_button(self):
        return self.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div[6]/div/form/div[4]/button')


if __name__ == '__main__':
    from selenium.webdriver import Chrome
    driver = Chrome()
    base_url = 'https://booking.uz.gov.ua/en/'
    search = SearchScreen(driver, base_url).open()
    search.main_form.from_field.send_keys('Kiev')
    search.main_form.to_field.send_keys('Odesa')
    print(dir(search.main_form.search_button.send_keys('111')))
   # search.main_form.search_button.click()
    search.authorize_form.auth_form_activate.click()
    search.authorize_form.email_field.send_keys('111')
    search.authorize_form.pwd_field.send_keys('222')
    search.authorize_form.enter_button.click()

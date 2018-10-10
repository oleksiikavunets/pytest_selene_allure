from pypom import Page, Region
from selenium.webdriver.common.by import By


class LoginScreen(Page):

    URL_TEMPLATE = '/authorization/'

    @property
    def login_form(self):
        root = self.find_element(By.XPATH, '//*[@id="auth-form"]')
        return LoginForm(self, root=root)


class LoginForm(Region):
    @property
    def email_field(self):
        return self.find_element(By.XPATH, '//*[@id="auth-form"]/form/input')

    @property
    def pwd_field(self):
        return self.find_element(By.XPATH, '//*[@id="auth-form"]/form/div[2]/input')

    @property
    def enter_button(self):
        return self.find_element(By.XPATH, '//*[@id="auth-form"]/form/div[4]/button')


if __name__ == '__main__':
    from selenium.webdriver import Chrome
    driver = Chrome()
    base_url = 'https://booking.uz.gov.ua/en/'
    login = LoginScreen(driver, base_url).open()
    login.login_form.email_field.send_keys('111')
    login.login_form.pwd_field.send_keys('222')
    login.login_form.enter_button.click()


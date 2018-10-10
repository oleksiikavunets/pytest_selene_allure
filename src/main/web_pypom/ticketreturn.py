from pypom import Page, Region
from selenium.webdriver.common.by import By
from time import sleep


class TicketReturn(Page):

    URL_TEMPLATE = 'cabinet/return_ticket/'

    @property
    def return_form(self):
        root = self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form')
        return ReturnForm(self, root=root)


class ReturnForm(Region):
    @property
    def uid(self):
        return self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form/div[1]/div/input')

    @property
    def fiscal_code(self):
        return self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form/div[2]/input')

    @property
    def last_name(self):
        return self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form/div[3]/input')

    @property
    def first_name(self):
        return self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form/div[4]/input')

    @property
    def return_button(self):
        return self.find_element(By.XPATH, '//*[@id="wrapper"]/div[1]/form/div[6]/button')


if __name__ == '__main__':
    from selenium.webdriver import Chrome
    driver = Chrome()
    base_url = 'https://booking.uz.gov.ua/en/'
    return_ticket = TicketReturn(driver, base_url).open()
    sleep(15)
    return_ticket.return_form.uid.send_keys('drgd')
    return_ticket.return_form.fiscal_code.send_keys('sddfv')
    return_ticket.return_form.last_name.send_keys('srgetfb')
    return_ticket.return_form.first_name.send_keys('dsrgfrdtv')
    return_ticket.return_form.last_name.send_keys('dsvfdf')
    return_ticket.return_form.return_button.click()

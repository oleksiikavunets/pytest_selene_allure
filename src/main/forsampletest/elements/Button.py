from selene.support.jquery_style_selectors import s


class Button:

    def __init__(self, locator):
        self.btn = s(locator)


    def click(self):
       self.btn.click()


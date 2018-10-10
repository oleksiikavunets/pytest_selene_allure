from src.main.web.controls.basecontrol import *
from src.main.web.controls.checker import it_is_what_it_is
from selene.api import s


# @it_is_what_it_is
class Button(BaseControl):
    __slots__ = 'is_displayed',

    def __init__(self, selector):
        self.button = s(selector)

    def __getattr__(self, item):
        if item in dir(self.button):
            return getattr(self.button, item)
        else:
            pass

    def click(self):
        if self.button.is_displayed():
            return getattr(self.button, 'click')()
        else:
            pass
    # return self.button.click()

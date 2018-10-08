from new_job.controls.basecontrol import *
from new_job.controls.checker import it_is_what_it_is
from selene.api import s


#@it_is_what_it_is
class Field(BaseControl):

    __slots__ = 'is_displayed'

    def __init__(self, selector):
        self.field = s(selector)

    def __getattr__(self, item):
        if item in dir(self.field):
            return getattr(self.field, item)
        else:
            pass

    def send_keys(self, keys):
        if self.field.is_displayed():
            return self.field.send_keys(keys)
        else:
            pass

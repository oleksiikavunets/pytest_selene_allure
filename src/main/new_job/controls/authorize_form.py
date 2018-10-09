from src.main.new_job.controls.basecontrol import *
from selene.api import s
from src.main.new_job.controls.button import *
from src.main.new_job.controls.textfield import *
from selene.api import *
from src.main.new_job.searcher.searchby import search


class Form(BaseControl):
    def __init__(self, selector):
        self.selector = s(selector[0])
        self.elements = selector[1]

    def __getattr__(self, name):

        if name in self.elements:
            return globals()[BaseControl.splitcamel(name)](search(xpath=self.elements[name]))
           # return globals()[BaseControl.splitcamel(name)](by.xpath(self.elements[name]))



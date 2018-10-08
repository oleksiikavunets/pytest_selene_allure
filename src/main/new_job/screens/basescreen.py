from selene.api import config, browser
import re


class BaseScreen:

    @classmethod
    def open(cls, *urlarg):
        config.browser_name = 'chrome'
        if 'url' in dir(cls):
            browser.open_url(cls.url)
        else:
            browser.open_url(urlarg[0])

    @staticmethod
    def splitcamel(name):
        return re.sub('(?!^)([A-Z][a-z]+)', r' \1', name).split()[-1]

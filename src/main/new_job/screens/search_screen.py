from src.main.new_job.controls.button import Button
from src.main.new_job.controls.textfield import Field
from src.main.new_job.controls.authorize_form import Form
from src.main.new_job.screens.basescreen import BaseScreen


class SearchScreen(BaseScreen):

    url = '/'

   # def __init__(self):
    logoButton = 'body > div.b-page-header > div > div.top-row > a.uz-logo'
    fromField = '#search-frm > form > div.search-block > div.stations > div:nth-child(1) > input'
    toField = '#search-frm > form > div.search-block > div.stations > div:nth-child(3) > input'
    submitButton = '#search-frm > form > div.button > div > button'
    authorizeForm = ['#search-frm > form > div.search-block > div.opt > div.date '
                              '> input[type="text"]:nth-child(3)',
                              {'authorizeButton': '/html/body/div[1]/div/div[3]/div[6]/div/form/div[4]/button',
                               'emailField': '/html/body/div[1]/div/div[3]/div[6]/div/form/input',
                               'passwordField': '/html/body/div[1]/div/div[3]/div[6]/div/form/div[2]/input',
                               'activateAuthorizeButton': '/html/body/div[1]/div/div[3]/div[6]/a'}]

    def __getattribute__(self, name):
        if name in dir(BaseScreen):
            return getattr(BaseScreen, name)(object.__getattribute__(self, name))
        return globals()[object.__getattribute__(self, 'splitcamel')(name)](object.__getattribute__(self, name))

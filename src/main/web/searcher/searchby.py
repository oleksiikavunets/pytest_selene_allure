from selene.api import by


def search(**locator):
    locator_type = list(locator.keys())[0]
    if locator_type in dir(by):

        return getattr(by, locator_type)(locator[locator_type])
    else:
        pass

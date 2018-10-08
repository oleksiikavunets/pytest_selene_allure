
def it_is_what_it_is(cls):
    controls = {'Button': ['submit', 'link', 'link active'], 'Field': ['text', 'password', 'email']}

    def check_type(*args, **kwargs):
        if cls(*args, **kwargs).get_attribute('type') in controls[cls.__name__]:
            return cls(*args, **kwargs)
        else:
            pass
    return check_type


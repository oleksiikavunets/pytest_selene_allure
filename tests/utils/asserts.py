class Assert:

    @staticmethod
    def __getPrettyMessage__(shouldPass, message):
        messageraw = "Test expected to {} but didn't. {}"
        if shouldPass:
            return messageraw.format("Pass", message)
        else:
            return messageraw.format("Fail", message)

    @staticmethod
    def assert_with_condition(condition, shouldPass, **kwargs):

        if shouldPass:
            assert condition is True, Assert.__getPrettyMessage__(shouldPass, kwargs.get('message', ""))
        else:
            assert condition is False, Assert.__getPrettyMessage__(shouldPass, kwargs.get('message', ""))

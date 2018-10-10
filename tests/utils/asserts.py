class Assert:

    @staticmethod
    def __getPrettyMessage__(resolution, message):
        return f"Test expected to {resolution} but didn't. {message}"

    @staticmethod
    def assert_with_condition(condition, shouldPass, **kwargs):

        if shouldPass:
            assert condition is True, Assert.__getPrettyMessage__("Pass", kwargs.get('message', ""))
        else:
            assert condition is False, Assert.__getPrettyMessage__("Fail", kwargs.get('message', ""))

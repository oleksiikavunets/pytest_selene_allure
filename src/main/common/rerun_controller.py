from src.main.common.base_config import MAX_RUN


class RerunController:

    def __init__(self):
        self._current_amount_of_runs = 0
        self.test = ""

    def add_test_to_listener(self, test):
        self.test = test
        print("ADDED TEST TO LISTEN")
        print(self.test)

    def add_rerun(self):
        self._current_amount_of_runs = self._current_amount_of_runs + 1

    def are_reruns_out(self):
        return self._current_amount_of_runs >= MAX_RUN

    def is_test_listened(self, test):
        print("CHECKING TEST TO BE LISTENED: ")
        print(self.test)
        return str(test) in str(self.test) or str(self.test) in str(test)


rerun_controller = RerunController()

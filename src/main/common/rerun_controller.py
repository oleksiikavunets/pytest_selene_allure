from src.main.common.base_config import MAX_RUN


class RerunController:

    def __init__(self):
        self._current_amount_of_runs = MAX_RUN
        self.test = ""

    def add_test_to_listener(self, test):
        self.test = test
        print("ADDED TEST TO LISTEN")
        print(self.test)

    def add_run(self):
        self._current_amount_of_runs = self._current_amount_of_runs - 1
        print("AMOUNT OF RUNS: " + str(self._current_amount_of_runs))

    def reset_runs(self):
        self._current_amount_of_runs = 0
        print("RESET RUNS!!!!")

    def are_reruns_out(self):
        return self._current_amount_of_runs == 0

    def is_test_listened(self, test):
        print("CHECKING TEST TO BE LISTENED: ")
        print(self.test)
        return str(test) in str(self.test) or str(self.test) in str(test)


rerun_controller = RerunController()

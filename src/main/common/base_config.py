import yaml


class BaseConfig:

    def __init__(self):
        self.config = self._loadConfig()
        self.test_session_started = False

    @staticmethod
    def _loadConfig():
        with open("config.yaml", "r") as yaml_config:
            return yaml.load(yaml_config)

    def set_test_session_started(self):
        self.test_session_started = True

    def set_test_session_closed(self):
        self.test_session_started = False


bc = BaseConfig()

MAX_RUN = bc.config["max_run"]
REMOTE = bc.config["remote"]
HOST = bc.config["host"]
PORT = str(bc.config["port"])
BASE_URL = bc.config["url"]


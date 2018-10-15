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

EMAIL = bc.config["email"]
PASSWORD = bc.config["password"]
MAX_RUN = bc.config["max_run"]
REMOTE_RUN = bc.config["remote_run"]
REMOTE_HOST = bc.config["remote_host"]
REMOTE_PORT = str(bc.config["remote_port"])
BASE_URL = bc.config["base_url"]


import pytest
from flaky import flaky
from selene import config
from time import sleep
from src.main.common.base_config import bc
from src.main.new_job.screens.search_screen import SearchScreen

#config.browser_name = 'chrome'

#SearchScreen.open()
#print(dir(SearchScreen))

@flaky(max_runs=bc.config["max_run"])
@pytest.mark.usefixtures("setup_class", "setup_function")
class TestUz:

    def test_qwert(self):
        config.browser_name = 'chrome'
        SearchScreen.open()

       # sleep(3)
     #   search = SearchScreen()
     #   search.open
        sleep(3)

#TestUz().test_qwert()

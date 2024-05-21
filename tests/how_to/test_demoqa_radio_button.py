import pytest
from tests.testbase import *
import time

class TestSuite:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get
        web = setWebDriver
        get = Locators(web)

        get.page("https://demoqa.com/radio-button")
        title = web.title
        assert title == "DEMOQA"

        yield
        web.quit()
        
    def test_TC1_click_buttons(self, precondition):
        get.bySelector('.custom-control-label[for="yesRadio"').click()
        get.bySelector('.custom-control-label[for="impressiveRadio"]').click()
        rb=get.bySelector('#noRadio')
        assert not rb.is_enabled(), "rb is enabled, which is expected"
    

if __name__ == '__main__':
    pytest.main()
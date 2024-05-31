import pytest
from tests.testbase import *
from selenium.common.exceptions import TimeoutException

import time

class Test_GX3_116_Button:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get
        web = setWebDriver
        get = Locators(web)

        get.page("https://demoqa.com/buttons")
        title = web.title
        assert title == "DEMOQA"
    
        yield
        web.quit()
        
    def test_TC01_double_clickme(self, precondition):
        dc_button = get.bySelector('#doubleClickBtn')
        get.double_click_command(dc_button) 
        time.sleep(3)
        assert get.wait_until_visible_by_text('You have done a double click')
       
    def test_TC02_right_clickme(self, precondition):
        rc_button = get.bySelector('#rightClickBtn')
        get.right_click_command(rc_button)
        get.scroll_down_200pixels
        assert get.wait_until_visible_by_text('You have done a right click')
     
    def test_TC03_clickme_dymanic(self, precondition):
        get.byXpath("(//button[contains(@class, 'btn-primary') and contains(text(), 'Click Me')])[3]").click()
        get.scroll_down_200pixels
        assert get.wait_until_visible_by_text('You have done a dynamic click')
       
       
if __name__ == '__main__':
    pytest.main()
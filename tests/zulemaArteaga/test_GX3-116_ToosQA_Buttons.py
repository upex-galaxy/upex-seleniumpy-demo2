import pytest
from tests.testbase import *
from selenium.common.exceptions import TimeoutException

import time

class Test_GX3_116_Button:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)

        get.page("https://demoqa.com/buttons")
        title = web.title
        assert title == "DEMOQA"
    
        yield
        web.quit()
        
    def test_TC01_double_clickme(self, precondition):
        dc_button = get.bySelector('#doubleClickBtn')
        do.double_click_command(dc_button) 
        time.sleep(3)
        assert do.wait_until_visible_by_text('You have done a double click')
       
    def test_TC02_right_clickme(self, precondition):
        rc_button = get.bySelector('#rightClickBtn')
        do.right_click_command(rc_button)
        do.scroll_down_by_pixels(200)
        assert do.wait_until_visible_by_text('You have done a right click')
     
    def test_TC03_clickme_dymanic(self, precondition):
        get.byXpath("(//button[contains(@class, 'btn-primary') and contains(text(), 'Click Me')])[3]").click()
        do.scroll_down_by_pixels(300)
        assert do.wait_until_visible_by_text('You have done a dynamic click')
       
       
if __name__ == '__main__':
    pytest.main()
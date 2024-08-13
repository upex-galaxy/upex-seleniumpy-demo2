from tests.testbase import *

class Test_GX3_4668_Elements_Button:
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
        
    def test_double_clickme(self, precondition):
        '''TC01: Validate displayed message when successfully double click button'''
        wait(1) #Needed if add blocker is not running
        dc_button = get.bySelector('#doubleClickBtn')
        do.double_click_command(dc_button) 
        time.sleep(3)
        do.scroll_down_by_pixels(500) #Needed if add blocker is not running
        assert do.wait_until_visible_by_text('You have done a double click')
       
    def test_right_clickme(self, precondition):
        '''TC02: Validate succesfully click button'''
        rc_button = get.bySelector('#rightClickBtn')
        do.right_click_command(rc_button)
        do.scroll_down_by_pixels(200)
        assert do.wait_until_visible_by_text('You have done a right click')
     
    def test_clickme_dymanic(self, precondition):
        '''TC03: Validate succesfully click button with dynamic identifier'''
        do.scroll_down_by_pixels(100)
        get.byXpath("(//button[contains(@class, 'btn-primary') and contains(text(), 'Click Me')])[3]").click()
        do.scroll_down_by_pixels(300)
        assert do.wait_until_visible_by_text('You have done a dynamic click')
       
       
if __name__ == '__main__':
    pytest.main()
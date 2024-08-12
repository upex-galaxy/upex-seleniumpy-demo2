from tests.testbase import *

class Test_GX3_4652_Elements_Radio_Buttons:
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
        
    def test_click_yes(self, precondition):
        '''TC01: Validate successfully click yes'''
        get.bySelector('.custom-control-label[for="yesRadio"').click()
        assert get.byXpath("//p[@class='mt-3']/span[text()='Yes']")
        
    def test_click_impresive(self, precondition):
        '''TC02: Validate successfully click impresive'''
        get.bySelector('.custom-control-label[for="impressiveRadio"]').click()
        assert get.byXpath("//p[@class='mt-3']/span[text()='Impressive']")

    def test_113_no_click(self, precondition):
        'TC03: Validate no click on button'
        rb=get.bySelector('#noRadio')
        assert not rb.is_enabled(), "rb is enabled, which is expected"


if __name__ == '__main__':
    pytest.main()
from tests.testbase import *

class Test_GX3_113_ToolsQA_Radio_Buttons:
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
        
    def test_TC01_click_yes(self, precondition):
        get.bySelector('.custom-control-label[for="yesRadio"').click()
        assert get.byXpath("//p[@class='mt-3']/span[text()='Yes']")
        
    def test_TC02_click_impresive(self, precondition):
        get.bySelector('.custom-control-label[for="impressiveRadio"]').click()
        assert get.byXpath("//p[@class='mt-3']/span[text()='Impressive']")

    def test_TC03_113_no_click(self, precondition):
        rb=get.bySelector('#noRadio')
        assert not rb.is_enabled(), "rb is enabled, which is expected"


if __name__ == '__main__':
    pytest.main()
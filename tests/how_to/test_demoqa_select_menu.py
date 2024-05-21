import pytest
from tests.testbase import *
import time

class TestSuite:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get
        web = setWebDriver
        get = Locators(web)

        get.page("https://demoqa.com/select-menu")
        title = web.title
        assert title == "DEMOQA"

        yield
        web.quit()
        
    def test_TC1_select_value(self, precondition):
        option_ids = ["react-select-2-option-0-0","react-select-2-option-0-1","react-select-2-option-1-0","react-select-2-option-1-1","react-select-2-option-2","react-select-2-option-3"]
        for option_ids in option_ids:
            web.execute_script("window.scrollBy(0, {})".format(200))
            dropdown = get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[1]").click()
            get.byID(option_ids).click()

    def test_TC2_select_one(self, precondition):
        select_title = ["react-select-3-option-0-0","react-select-3-option-0-1","react-select-3-option-0-2","react-select-3-option-0-3","react-select-3-option-0-4","react-select-3-option-0-5"]
        for select_title in select_title:
            web.execute_script("window.scrollBy(0, {})".format(200))
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[2]").click()
            get.byID(select_title).click()
        
    def test_TC3_old_style_menu(self, precondition):
        oldStyleMenu = get.byID("oldSelectMenu")
        values = ["red","1","2","3","4","5","6","7","8","9","10"]
        for value in values:
            get.select_by_value(oldStyleMenu, value)
            
    def test_TC4_multi_drop_down(self, precondition):
        web.execute_script("window.scrollBy(0, {})".format(300))
        color_dropdown_ids = ["react-select-4-option-0","react-select-4-option-2","react-select-4-option-3","react-select-4-option-1"]
        for color_id in color_dropdown_ids:
            web.execute_script("window.scrollBy(0, {})".format(100))
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[3]").click()
            get.byID(color_id).click()
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[3]").click()
               
    def test_TC5_standart_multi_select(self, precondition):
        multi_select = get.byID("cars")
        values = ["volvo", "saab", "opel", "audi"]
        for value in values:
            get.select_by_value(multi_select,value)  

if __name__ == '__main__':
    pytest.main()

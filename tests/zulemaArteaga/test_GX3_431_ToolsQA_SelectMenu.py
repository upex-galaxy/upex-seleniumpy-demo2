from tests.testbase import *

class Test_GX3_431_ToolsQA_SelectMenu:
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
    
    def test_TC1_select_value_random(self, precondition):
        base_id = "react-select-2-option-"                      # All "Select Option" start with this id
        suffixes = ["0-0", "0-1", "1-0", "1-1", "2", "3"]       # The suxfixes are all the options available in this dropdown
        for x in range(len(suffixes)):
            random_suffix = random.choice(suffixes)             # Select Option randomly
            option_id = base_id + random_suffix
            get.scroll_down_200pixels()
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[1]").click()
            wait(3)
            get.byID(option_id).click()
                       
    def test_TC2_select_one(self, precondition):
        base_id = "react-select-3-option-"
        suffixes = ["0-0","0-1","0-2","0-3","0-4","0-5"]
        for x in range(len(suffixes)):
            random_suffix = random.choice(suffixes)             # Select One randomly
            option_id = base_id + random_suffix
            get.scroll_down_300pixels()
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[2]").click()
            wait(2)
            get.byID(option_id).click()
        
    def test_TC3_old_style_menu(self, precondition):
        oldStyleMenu = get.byID("oldSelectMenu")
        values = ["red","1","2","3","4","5","6","7","8","9","10"]
        for value in values:
            get.select_by_value(oldStyleMenu, value)
            
    def test_TC4_multi_drop_down(self, precondition):
        base_id = "react-select-4-option-"
        suffixes = ["0", "2", "3", "1"]
        get.scroll_down_400pixels()
        for suffix in suffixes:
            color_id = base_id + suffix
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
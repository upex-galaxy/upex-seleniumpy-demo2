from tests.testbase import *

class Test_GX3_431_ToolsQA_SelectMenu:
    
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)
        
        get.page("https://demoqa.com/select-menu")
        title = web.title
        assert title == "DEMOQA"


        yield
        web.quit()
    
    # Scenario 1: User selects one element'''
    def test_select_value_random(self, precondition):
        '''TC01: ToolsQA | Widgets | Dropdown | Select Menu | Validate succesfully Select Value from drop down '''
        def select_dropdown_random_option(): 
            options = get.byXpaths(
                '//*[starts-with(@id, "react-select")][contains(@id, "option")]')
            count = len(options)
            random_index = random.randint(0, count - 1)
            given_element = options[random_index]
            given_text = given_element.text

            given_element.click()
            return given_text

        get.contains('Select Option').click()
        select_dropdown_random_option()

        def test_select_one():
            '''TC02: ToolsQA | Widgets | Dropdown | Select Menu | 
            Validate succesfully Select One from drop down '''
            
            options = get.byXpaths(
                '//*[starts-with(@id, "react-select-3")][contains(@id, "option")]')
            count = len(options)
            random_index = random.randint(0, count - 1)
            given_element = options[random_index]
            given_text = given_element.text

            given_element.click()
            return given_text

        get.contains('Select Title').click()
        test_select_one()
        
        def test_old_style_menu():
            '''TC03: ToolsQA | Widgets | Dropdown | Select Menu | 
            Validate succesfully select Old Style Select Menu'''
            
            options = get.byID("oldSelectMenu")
            values = ["red","1","2","3","4","5","6","7","8","9","10"]
            for value in values:
                do.select_by_value(options, value)
        actual_value = test_old_style_menu()
    
    # Scenario 2: User selects one or more elements from "Multiselect drop down" menu'''    
    def test_multi_drop_down(self, precondition):
        '''TC04: ToolsQA | Widgets | Dropdown | Select Menu | 
        Validate succesfully selects Multiselect drop down'''
        
        base_id = "react-select-4-option-"
        suffixes = ["0", "2", "3", "1"]
        do.scroll_down_by_pixels(400)
        for suffix in suffixes:
            color_id = base_id + suffix
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[3]").click()
            get.byID(color_id).click()
            get.byXpath("(//*[contains(concat(' ', @class, ' '), ' css-1hwfws3')])[3]").click()
    
    # Scenario 3: User selects several elements from "Standard multi select" menu'''    
    def test_standart_multi_select(self, precondition):
        '''TC05: ToolsQA | Widgets | Dropdown | Select Menu | 
        Validate succesfully selects Multiselect Dropdown'''
        
        multi_select = get.byID("cars")
        values = ["volvo", "saab", "opel", "audi"]
        for value in values:
            do.select_by_value(multi_select,value)  

if __name__ == '__main__':
    pytest.main()
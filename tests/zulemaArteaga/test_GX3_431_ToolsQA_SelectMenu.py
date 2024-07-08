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
    
    # Scenario 1: User selects one element
    def test_select_one(self, precondition):
        def select_option():
            '''TC01: Validate select option in dropdowns "Select Value" ("Select Option")'''
            do.select_an_option_randomly('//*[starts-with(@id, "react-select")][contains(@id, "option")]')
        get.contains('Select Option').click()
        select_option()

        def select_title():
            '''TC02: Validate succesfully Select One from drop down '''
            do.select_an_option_randomly('//*[starts-with(@id, "react-select-3")][contains(@id, "option")]')
        get.contains('Select Title').click()
        select_title()
            
        def test_old_style_menu():
            '''TC03: Validate successfully “Select Old Style Select Menu” from drop down'''
            select_menu_element = get.byID("oldSelectMenu")
            select_menu = Select(select_menu_element)
            option_values = [option.get_attribute("value") for option in select_menu.options]
            for value in option_values:
                select_menu.select_by_value(value)
        test_old_style_menu()
    
    # Scenario 2: User selects one or more elements from "Multiselect drop down" menu'''    
    def test_multi_drop_down(self, precondition):
        '''TC04: Validate succesfully selects Multiselect drop down'''
        do.scroll_down_by_pixels(250)
        select_option = get.contains("Select...")
        select_option.click()
        time.sleep(1)
        color_options = get.byXpaths(
                '//*[starts-with(@id, "react-select-4")][contains(@id, "option")]')
        for color in color_options:
            color.click()
    
    # # Scenario 3: User selects several elements from "Standard multi select" menu'''    
    def test_standart_multi_select(self, precondition):
        '''TC05: Validate succesfully selects Multiselect Dropdown'''
        do.scroll_down_by_pixels(300)
        select_car = get.byID("cars")
        car_option = get.byTags("option")
        for car in car_option:
            car.click()
            time.sleep(3) 

if __name__ == '__main__':
    pytest.main()
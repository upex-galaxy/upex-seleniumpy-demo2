from tests.testbase import *

class Test_GX3_4660_Elements_Checkbox:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)

        get.page("https://demoqa.com/checkbox")
        title = web.title
        assert title == "DEMOQA"
    
        yield
        web.quit()
        
    def test_select_all(self, precondition):  
        '''Validate ALL CHECKBOXES ARE SELECTED when clicking Home'''
        checkboxes = get.bySelectors('input[type="checkbox"]')
        get.contains("Home").click()

        selected_checkboxes = [checkbox.is_selected() for checkbox in checkboxes]
        assert selected_checkboxes, f"Not all checkboxes are selected! Selected checkboxes are: {selected_checkboxes}"
       
    def test_expand_all(self, precondition):
        '''Validate EXPAND ALL when clicking "+"'''
        expand_all = get.bySelector("button.rct-option.rct-option-expand-all").click()
        
        expanded_tree = get.bySelector("#tree-node > div > button.rct-option.rct-option-expand-all")
        assert expanded_tree, "Checkbox tree should be present after expanding all."
     
    def test_collapse_all(self, precondition):
        '''Validate COLLAPSE ALL when clicking "-"'''
        expand_all = get.bySelector("button.rct-option.rct-option-expand-all").click()
        collapse_all = get.bySelector("button.rct-option.rct-option-collapse-all").click()
        
        collapsed_tree = get.bySelector("#tree-node > div > button.rct-option.rct-option-collapse-all")
        assert collapsed_tree, "Checkbox tree should NOT be present after collapsing all."
        
    def test_random_checkbox(self, precondition):
        '''Validate select random checkboxes'''
        expand_all = get.bySelector("button.rct-option.rct-option-expand-all").click()
        random_ckeckbox = do.click_randomly("//span[@class='rct-checkbox']")
        assert get.bySelector("*:checked")
        
if __name__ == '__main__':
    pytest.main()
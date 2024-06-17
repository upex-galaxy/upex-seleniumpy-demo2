from tests.testbase import *

class Test_GX3_109_ToolsQA_BookStore:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)

        '''User must be in this page'''
        get.page("https://demoqa.com/books")
        title = web.title
        assert title == "DEMOQA"

        yield
        web.quit()
    
    def test_order_by(self, precondition):
        '''TC04: ToolsQA | Book Store Applications | Book Store |
        Validate successfully filter alphabetically in search bar'''

        # NOT RUNING - sorting by title needs to be fixed.
        # get.byXpath("//*[.='Title']").click()
        # title_list = do.get_table_data(ordered_by='titles')
        # assert title_list == sorted(title_list), "Titles are not sorted alphabetically"
        
        get.byXpath("//*[.='Author']").click()  # Click on the "Author" sorting option
        author_list = do.get_table_data(ordered_by='author') # Getting the table data after clicking to sort by author
        assert author_list == sorted(author_list), "Authors are not sorted alphabetically" # Verifying if the displayed information is correctly sorted
        
        get.byXpath("//*[.='Publisher']").click()  # Click on the "Title" sorting option
        publisher_list = do.get_table_data(ordered_by='publisher')
        assert publisher_list == sorted(publisher_list), "Publishers are not sorted alphabetically"


if __name__ == '__main__':
    pytest.main()
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
    
    
    def test_filter_books_in_search_bar(self, precondition):
        '''TC01: ToolsQA | Book Store Applications | Book Store |
        Validate successfully filter books in search bar'''
        
        search_bar = get.byID('searchBox')
        with open ('tests/zulemaArteaga/data/GX3_109_seach_bar_queries.txt', 'r') as file:
            queries = file.readlines()
            
        for query in queries:
            query = query[:2] # Type the first 2 letters of each query
            search_bar.clear()
            search_bar.send_keys(query.strip()) # Remove spaces
        
        search_results_cells = get.bySelector('div[role="gridcell"]')
        
        for result in search_results_cells:
            title = search_results_cells[1].text
            author = search_results_cells[2].text
            publisher = search_results_cells[3].text 
        
        assert query == (title[:2] or author[:2] or publisher [:2]), f"Search bar not working correctly"
    
    # def test_log_in(self, precondition):
    #     '''TC02: ToolsQA | Book Store Applications | Book Store |
    #     Validate successfully log in'''
 
    # def test_log_out(self, precondition):
    #     '''TC03: ToolsQA | Book Store Applications | Book Store |
    #     Validate successfully log out'''
    
    
    def test_order_by(self, precondition):
        '''TC04: ToolsQA | Book Store Applications | Book Store | 
        Validate successfully filter alphabetically by clickiing filter'''

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
    
    # def test_filter_books_in_search_bar(self, precondition):
    #     '''TC05: ToolsQA | Book Store Applications | Book Store |
    #     Validate successfully display book information'''


if __name__ == '__main__':
    pytest.main()
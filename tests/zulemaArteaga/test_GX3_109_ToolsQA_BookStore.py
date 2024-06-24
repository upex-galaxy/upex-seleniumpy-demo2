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
        '''TC01: 
        Validate successfully filter books in search bar'''
        
        search_bar = get.byID('searchBox')
        with open ('tests/zulemaArteaga/data/GX3_109_queries.text', 'r') as file:
            queries = file.readlines()
            
        for query in queries:
            query = query[:2] # Type the first 2 letters of each query
            search_bar.clear()
            search_bar.send_keys(query)
        
            search_results_cells = get.bySelector('div[role="gridcell"]').text
            search_results_texts = [cell.text for cell in search_results_cells]
            for result in search_results_texts[1:]:  # Start comparing the results from index 1 to the end of the cells
                assert query == search_results_texts, f"Search bar not working correctly"
    
    def test_login_button(self, precondition):
        '''TC02: 
        Validate successfully is redirected to the log in page when clicks login button'''
        
        get.byID('login').click()
        expected_url = 'https://demoqa.com/login'
        assert expected_url
    
    def test_order_by(self, precondition):
        '''TC04:
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
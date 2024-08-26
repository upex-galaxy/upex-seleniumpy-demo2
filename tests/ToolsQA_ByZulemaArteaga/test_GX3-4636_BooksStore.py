import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from tests.testbase import Locators, Actions_to_execute

class Test_GX3_109_ToolsQA_BookStore:
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global get
        global web
        global do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)
        
        get.page('https://demoqa.com/books')
        title = web.title
        assert title == 'DEMOQA', f"Expected title 'DEMOQA' but got '{title}'"
        
        yield
        
        web.quit()

    def test_filter_books_in_search_bar(self, precondition):
        """TC01: Validate successfully filter books in search bar when typing two letters"""
        queries = do.get_table_data(ordered_by='titles')
        search_bar = get.byID('searchBox')
        for query in queries:
            query = query[:2]
            search_bar.clear()
            search_bar.send_keys(query)
            search_results_cells = get.bySelectors('div[role="gridcell"]')
            search_results_texts = [cell.text for cell in search_results_cells]
            #Use this when you want to ensure that the query appears in at least one of the search results.
            assert any(query in text for text in search_results_texts), f"'{query}' not found in search results." 
            # Use if the expectation is that ALL results should match the query.
            # assert all(query in text for text in search_results_texts), f"Search bar not working correctly for query '{query}'"
        
    def test_login_button(self, precondition): 
        #Currently not testing logout since I don't have the credentials for login
        """TC02: Validate successfully is redirected to the login page when clicks login button"""
        get.byID('login').click()
        expected_url = 'https://demoqa.com/login'
        assert web.current_url == expected_url, \
            f"Expected URL '{expected_url}' but got '{web.current_url}'"
    
    def test_order_by(self, precondition):
        """TC04: Validate successfully filter alphabetically in search bar when clicking column header"""
        get.byXpath('//*[text()="Author"]').click()
        author_list = do.get_table_data(ordered_by='author')
        assert author_list == sorted(author_list), \
            f"Authors are not sorted alphabetically: {author_list}"
        
        get.byXpath('//*[text()="Publisher"]').click()
        publisher_list = do.get_table_data(ordered_by='publisher')
        assert publisher_list == sorted(publisher_list), \
            f"Publishers are not sorted alphabetically: {publisher_list}"

if __name__ == '__main__':
    pytest.main()

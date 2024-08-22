from tests.testbase import *
class Test_GX3_4595_ToolsQA_TextBox:
    
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)

        get.page("https://demoqa.com/text-box")
        
        title = web.title
        assert title == "DEMOQA"

        yield
        web.quit()
    
    def test_fill_fullname(self, precondition):
        '''TC01: Verify if log message matches the added inputs in the form'''
        
        # Importing data from cvs file to fill out the Text Box form
        with open('tests/ToolsQA_ByZulemaArteaga/data/GX3_4595_login_data.csv', 'r') as file:
            data = csv.DictReader(file)
            
            # Filling out the form with the data in file  
            for row in data:
                name = do.fill_input_byID_identifier("userName", row['name'])
                email = do.fill_input_byID_identifier("userEmail", row['email'])
                current_address = do.fill_input_byID_identifier("currentAddress", row['current_address'])
                permanent_address = do.fill_input_byID_identifier("permanentAddress", row['permanent_address'])
            
            # Submit form
                do.scroll_down_by_pixels(200)
                get.byID("submit").click()

            # Verify if typed input matches the log message displayed
                def input_value_matches_log(input_element, log_label: str):
                    input_value = input_element.get_attribute("value")
                    log_message_no_label = do.get_log_message_no_label(log_label)
                    assert input_value == log_message_no_label, f"Mismatch, typed input doesn't match log message displayed"
                
                    input_value_matches_log(name, 'Name:')
                    input_value_matches_log(email, 'Email:')
                    input_value_matches_log(current_address, 'Current Address :')
                    input_value_matches_log(permanent_address, 'Permananet Address :')           
                
                web.refresh()
    
    def test_fill_invalid_email(self, precondition):
        ''' TC02: Validating that when adding an INVALID email and clicking submit, a red input border is displayed'''

        email = get.byID("userEmail")
        email.send_keys("zulemagmail.com")
        do.scroll_down_by_pixels(400)
        get.byID("submit").click()
        email_text = email.text
        # Email rules:
        contains_at = r'@'                              # Invalid if Does not contain “@”
        alphanumeric_before_at = r'\w+@'                # Invalid if Does not contain (minimum) 1 alphanumeric character before “@”
        alphanumeric_after_at = r'@\w+'                 # Invalid if Does not contain (minimum) 1 alphanumeric character after “@”
        dot_after_alphanumeric_after_at = r'@\w+\.'     # Invalid if Does not contain “.” after: 1 alphanumeric character after “@”.
        alphanumeric_after_dot = r'@\w+\.\w+'           # Invalid if Does not contain (minimum) 2 alphanumeric characters after “.”
        if not (re.search(contains_at, email_text) and
                    re.search(alphanumeric_before_at, email_text) and
                    re.search(alphanumeric_after_at, email_text) and
                    re.search(dot_after_alphanumeric_after_at, email_text) and
                    re.search(alphanumeric_after_dot, email_text)):
            # Assert the error-form to verify a red border is displayed when adding invalid data in the field email
            assert get.bySelector(".mr-sm-2.field-error.form-control")    
   
   
if __name__ == '__main__':
    pytest.main()
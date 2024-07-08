from tests.testbase import *
from tests.utils.asserts import Expect
from tests.utils.locators import Locators

class Test_GX3_118_ToolsQA_TextBox:
    
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
    
    def test__fill_fullname(self, precondition):
        '''TC01: Verify if log message matches the added inputs in the form'''
        
        with open('tests/zulemaArteaga/data/GX3_118_login_data.csv', 'r') as file:
            data = csv.DictReader(file)
            for row in data:
                name = row['name']
                email = row['email']
                current_address = row['current_address']
                permanent_address = row['permanent_address']

                # Filling out the form
                name_input = get.byID("userName")
                name_input.send_keys(name)
                
                email_input = get.byID("userEmail")
                email_input.send_keys(email)
                
                current_address_input = get.byID("currentAddress")
                current_address_input.send_keys(current_address)
                
                permanent_address_input= get.byID("permanentAddress")
                permanent_address_input.send_keys(permanent_address)
                
                do.scroll_down_by_pixels(200)
                get.byID("submit").click()
                

                name_input_value = name_input.get_attribute("value")          # Getting the attribute of the input
                log_message_no_label = do.get_log_message_no_label('Name:')   # Getting the log message attribute without label
                assert  name_input_value == log_message_no_label                        
                
                email_input_value = email_input.get_attribute("value")   
                log_message_no_label = do.get_log_message_no_label('Email:')  
                assert  email_input_value == log_message_no_label  
                               
                current_address_input_value = current_address_input.get_attribute("value")   
                log_message_no_label = do.get_log_message_no_label('Current Address :')  
                assert  current_address_input_value == log_message_no_label  
                   
                permanent_address_input_value = permanent_address_input.get_attribute("value")   
                log_message_no_label = do.get_log_message_no_label('Permananet Address :')  
                assert  permanent_address_input_value == log_message_no_label               
                
                web.refresh()
    
    def test_fill_invalid_email(self, precondition):
        ''' TC02: Validating that when adding an INVALID email and clicking submit, a red input border is displayed'''

        email = get.byID("userEmail")
        email.send_keys("zulemagmail.com")
        do.scroll_down_by_pixels(300)
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
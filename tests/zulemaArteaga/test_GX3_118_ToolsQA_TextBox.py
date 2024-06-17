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
        '''TC01: ToolsQA | Elements | Text Box: Fill Form and Submit |
        Verify if log message matches the added inputs in the form'''
        
        #Filling out the form
        name = get.byID("userName")
        input_name = name.send_keys("Zulema")
        
        email = get.byID("userEmail")
        email.send_keys("zulema@gmail.com")
        
        current_address = get.byID("currentAddress")
        current_address.send_keys("xxx xxxx, xxx, usa")
        
        permanent_address= get.byID("permanentAddress")
        permanent_address.send_keys("xxx xxxx, xxx, usa")
        
        get.byID("submit").click()
        
        # Verifying if added input mathces the log message displayed
        do.test_compare_input_vs_log(name, "Name:")
        do.test_compare_input_vs_log(email, "Email:")
        do.test_compare_input_vs_log(current_address, "Current Address :")
        do.test_compare_input_vs_log(permanent_address, "Permananet Address :")

    
    def test_fill_invalid_email(self, precondition):
        ''' TC02: ToolsQA | Elements | Text Box: Fill Form and Submit |
        Validating that when adding an INVALID email and clicking submit, a red input border is displayed'''
        
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
        if (re.search(contains_at, email_text) or
                    re.search(alphanumeric_before_at, email_text) or
                    re.search(alphanumeric_after_at, email_text) or
                    re.search(dot_after_alphanumeric_after_at, email_text) or
                    re.search(alphanumeric_after_dot, email_text)):
            pass
        else:
            assert get.bySelector(".mr-sm-2.field-error.form-control")          # Verify a red border is displayed when adding invalid data in the field email
   
if __name__ == '__main__':
    pytest.main()
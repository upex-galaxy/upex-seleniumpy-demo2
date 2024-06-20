from tests.testbase import *

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
    
    def test_fill_out_text_box(self, precondition):
        
        name = get.byID("userName")
        input_name = name.send_keys("Zulema")
        
        email = get.byID("userEmail")
        email.send_keys("zulema@gmail.com")
       
        current_address = get.byID("currentAddress")
        current_address.send_keys("xxx xxxx, xxx, usa")
        
        permanent_address= get.byID("permanentAddress")
        permanent_address.send_keys("xxx xxxx, xxx, usa")
      
        get.byID("submit").click()
        
        
        input_value = name.get_attribute("value")                       # Getting the attribute of the added input to compare later with the log message
        log_message =get.byXpath("//p[contains(text(),'Name:')]").text  # Find the log message box and get it in text
        log_message_value = log_message[len("Name:"):]                  # Slicing to remove the label and be able to compare with the name input
        assert input_value == log_message_value                         # Compare if input matches the log message

        input_value = email.get_attribute("value")      # Getting the attribute of the added input to compare later with the log message                                 
        log_message =get.byXpath("//p[contains(text(),'Email:')]").text     # Find the log message box and get it in text
        log_message_value = log_message[len("Email:"):]                     # Slicing to remove the label and be able to compare with the input
        assert input_value == log_message_value                             # Compare if input matches the log message
   
        input_value = current_address.get_attribute("value")                            # Getting the attribute of the added input to compare later with the log message  
        log_message =get.byXpath("//p[contains(text(),'Current Address :')]").text      # Find the log message box and get it in text
        log_message_value = log_message[len("Current Address :"):]                      # Slicing to remove the label and be able to compare with the input
        assert input_value == log_message_value                                         # Compare if input matches the log message
    
        input_value = permanent_address.get_attribute("value")                      # Getting the attribute of the added input to compare later with the log message  
        log_message =get.byXpath("//p[contains(text(),'Permananet Address :')]").text      # Find the log message box and get it in text
        log_message_value = log_message[len("Permananet Address :"):]                      # Slicing to remove the label and be able to compare with the input
        assert input_value == log_message_value                                            # Compare if input matches the log message
    
    
    
    def test_adding_invalid_email(self, precondition):
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
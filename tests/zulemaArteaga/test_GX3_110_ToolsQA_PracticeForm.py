from tests.testbase import *

class Test_GX3_118_ToolsQA_TextBox:
    
    @pytest.fixture
    def precondition(self, setWebDriver: WebDriver):
        global web, get, do
        web = setWebDriver
        get = Locators(web)
        do = Actions_to_execute(web)

        get.page("https://demoqa.com/automation-practice-form")
        
        title = web.title
        assert title == "DEMOQA"

        yield
        web.quit()

    def test__fill_full_out_form(self, precondition):
            '''TC01: Verify that after submiting the form, a popup window is displayed confirming the submited information'''
            
            with open('tests/zulemaArteaga/data/GX3_110_PracticeForm_data.csv', 'r') as file:
                data = csv.DictReader(file)
            
            # Filling out the form with the data in file  
                for row in data:
                    name = do.fill_input_byID_identifier("firstName", row['name'])
                    last_name = do.fill_input_byID_identifier("lastName", row['last_name'])
                    email = do.fill_input_byID_identifier('userEmail', row['email'])
                    
                    # Selecting Radio Buttons to select gender provided in data file
                    male = row['gender'] == "Male"
                    female = row['gender'] == "Female"
                    other = row['gender'] == "Other" 
                    if male:
                        get.byXpath("//*[starts-with(@class, 'custom-control') and contains(., 'Male')]").click()
                    elif female:
                        get.byXpath("//*[starts-with(@class, 'custom-control') and contains(., 'Female')]").click()
                    elif other:
                        get.byXpath("//*[starts-with(@class, 'custom-control') and contains(., 'Other')]").click()            
                    
                    mobile = do.fill_input_byID_identifier('userNumber', row['mobile'])
                    
                    # Select Date of birth
                    # birth_day = get.byID("dateOfBirthInput").click()
                    
                    subject_input = get.byID('subjectsInput')
                    subjects_list = [subject.strip() for subject in row['subjects'].strip('"').split(',')]
                    for subject in subjects_list:
                        subject_input.send_keys(subject[:3])  # Typing the first 3 letters of each subject
                        wait(1) # Waiting for the subject option to appear
                        subject_option = get.byXpath(f"//div[text()='{subject}']")
                        subject_option.click()
                        subject_input.click()
                 
                    do.scroll_down_by_pixels(400)
                    get.byID("submit").click()
        # Verify the submit information/confirmation window
                    assert get.contains("Thanks for submitting the form")
        # Closing the popup window
                    do.scroll_down_by_pixels(200)
                    get.byID("closeLargeModal").click()
                    web.refresh()
       

if __name__ == '__main__':
    pytest.main()
from tests.testbase import *
@pytest.mark.skip(reason="Currently not testing this")   
class Test_GX3_4644_ToolsQA_PracticeForm:
    
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

    def test_fill_out_form(self, precondition):
            '''TC01: Verify that after submiting the form with VALID data, a popup window is displayed confirming the submited information'''
            
            # Importing data from cvs file to fill out the practice form
            with open('tests/ToolsQA_ByZulemaArteaga/data/GX3-4644_PracticeForm_data.csv', 'r') as file:
                data = csv.DictReader(file)
            
            # Filling out the form with the data in file  
                for row in data:
                    name = do.fill_input_byID_identifier("firstName", row['name'])
                    last_name = do.fill_input_byID_identifier("lastName", row['last_name'])
                    email = do.fill_input_byID_identifier('userEmail', row['email'])
                    
            # Selecting Radio Buttons to select gender provided in data file
                    gender = row['gender']
                    if gender in ["Male", "Female", "Other"]:
                        get.byXpath(f"//*[starts-with(@class, 'custom-control') and contains(., '{gender}')]").click()           
                
            # Add mobile number
                    mobile = do.fill_input_byID_identifier('userNumber', row['mobile'])
                    
            # Select Date of birth
                    calendar_input = get.byID("dateOfBirthInput").click()
                    date = [date_part.strip() for date_part in row['date_of_birth'].strip('"').split(',')]
                    month, day, year = date[0].strip('"').split('/')
                    
                    do.select_dropdown_by_value("//div[contains(@class, 'react-datepicker__month-dropdown')]/select", month)
                    do.select_dropdown_by_value("//div[contains(@class, 'react-datepicker__year-dropdown')]/select", year)
                    day = get.byXpath( f"//div[contains(@class, 'react-datepicker__day') and text()='{day}']").click()
                    
            # Select subjects
                    wait(5)
                    subject_input = get.byID('subjectsInput')
                    subjects_list = [subject.strip() for subject in row['subjects'].strip('"').split(',')]
                    for subject in subjects_list:
                        subject_input.send_keys(subject[:3])  # Typing the first 3 letters of each subject
                        wait(.5) # Waiting for the subject option to appear
                        subject_option = get.byXpath(f"//div[text()='{subject}']")
                        subject_option.click()
                 
            # Select Hobbies
                    hobbies = [hobby.strip() for hobby in row['hobbies'].strip('"').split(',')] # Splitting the hobbies from the string
                    for hobby in hobbies:
                        try:
                            if hobby == 'Sports' : get.contains("Sports").click()
                            elif hobby == 'Reading': get.contains("Reading").click()
                            elif hobby == 'Music': get.contains("Music").click()
                        except NoSuchElementException: # If no hobbies
                            pass
                        
            # Add Address
                    current_address = do.fill_input_byID_identifier('currentAddress', row['current_address'])
                    
            # Submit form
                    do.scroll_down_by_pixels(300)
                    get.byID("submit").click()
                    
        # Verify the submit information/confirmation window
                    assert get.contains("Thanks for submitting the form")
                    
        # Closing the popup window and refresh page 
                    get.byID("closeLargeModal").click() 
                    web.refresh()

if __name__ == '__main__':
    pytest.main()
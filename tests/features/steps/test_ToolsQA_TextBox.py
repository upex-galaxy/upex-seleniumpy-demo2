from tests.testbase import *
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators
from tests.utils.asserts import Expect as expect
from pytest_bdd  import scenario, given, when, then

@step('I am at the Text Box Page "https://demoqa.com/text-box"')
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

@step('I add Full Name "{fullname}"')
def test_fill_fullname():
    name = get.byID("userName")
    input_name = name.send_keys("{fullname}")
    do.scroll_down_by_pixels(400)
    get.byID("submit").click()
    
@step('I add Email "{email}"')
def test_fill_valid_email():
    name = get.byID("userEmai")
    input_name = name.send_keys("{email}")
    
@step('I add Current Address"{current_address}"')
def test_fill_current_address():
    name = get.byID("currentAddress")
    input_name = name.send_keys("{current_address}")

@step('I add Permanent Address"{permanent_address}"')
def test_fill_permanent_address():
    name = get.byID("currentAddress")
    input_name = name.send_keys("{permanent_address}")

@step('I click on the Submit button')
def test_click_submit(): 
    do.scroll_down_by_pixels(400)
    get.byID("submit").click()
    
@step('I <should or should not> see a log message with the information submited in the form')
def test_TC06_fillout_complete_form_happy_path(self, precondition):
    def test_TC01_fill_fullname(self):
        pass  
    def test_TC02_fill_valid_email(self):
        pass
    def test_TC04_fill_current_address(self):
        pass
    def test_TC05_fill_permanent_address(self):
        pass
        
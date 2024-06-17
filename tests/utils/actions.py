from tests.testbase import *

class Actions_to_execute:
    def __init__(self, driver: WebDriver):
        global web, get
        self.web = driver
        get = Locators(self.web)
        
    def select_by_value(self, element: WebElement, value: str):
        select = Select(element)
        select.select_by_value(value)
        return select
    
    def double_click_command(self, element):
        action = ActionChains(self.web)
        action.double_click(element).perform()
        
    def right_click_command(self, element):
        action = ActionChains(self.web)
        action.context_click(element).perform()
        
    def wait_until_visible_by_text(self, text: str, timeout=10):
        # Esperar hasta que el texto este visible.
        try:
            WebDriverWait(self.web, timeout).until(
                    EC.presence_of_element_located((By.XPATH, f'//*[contains(text(),"{text}")]'))) 
            return True
        except TimeoutException:
            return False
        
    def wait_until_element_clickable(self, text: str, timeout=10):
        # Esperar hasta que se pueda hacer click al elemento
        WebDriverWait(self.web, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, f'//*[contains(text(),"{text}")]'))) 
        
    def scroll_down_by_pixels(self, pixels):
        self.web.execute_script("window.scrollBy(0, {})".format(pixels))
           
    def get_table_data(self, ordered_by=None):
        rows = get.bySelectors('div[class="rt-tr-group"]')
        table = []
        for row in rows:
            cells = row.find_elements(By.CSS_SELECTOR, 'div[role="gridcell"]')
            book_data = {
                'image': cells[0].text.strip(),
                'title': cells[1].text.strip(),
                'author': cells[2].text.strip(),
                'publisher': cells[3].text.strip()
            }
            table.append(book_data)  # Append each book_data dictionary to the table list
            
        ordered_list=[]
            # Filter and extract data based on ordered_by
        if ordered_by == 'titles':
            ordered_list = [row['title'] for row in table if row['title'].strip()] # Strip us used to remove the empty cells
        elif ordered_by == 'authors':
            ordered_list = [row['author'] for row in table if row['author'].strip()]
        elif ordered_by == 'publishers':
            ordered_list = [row['publisher'] for row in table if row['publisher'].strip()]
        return ordered_list
    
    def test_compare_input_vs_log(self, input_element, log_label):
            input_value = input_element.get_attribute("value") # Getting the input value
            log_message = get.byXpath(f"//p[contains(text(), '{log_label}')]").text # Getting the log message
            log_message_value = log_message[len(log_label):].strip()  # Removing label from the log message
            assert input_value == log_message_value, f"Input and log message don't match"
from tests.testbase import *

class Actions_to_execute:
    def __init__(self, driver: WebDriver):
        self.web = driver
        
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
        
  
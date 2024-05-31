from tests.testbase import *
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Locators:
    # * Definición de funciones para interactuar con elementos de la página
    def __init__(self, driver: WebDriver):
        self.web = driver

    def page(self, link: str):
        # Función para abrir una URL en el navegador web y maximizar la ventana
        self.web.maximize_window()
        self.web.get(link)

    def byDataTest(self, data_test: str):
        # Buscar elemento por data-test id
        return self.web.find_element(By.CSS_SELECTOR, f"[data-test={data_test}]")

    def byDataTests(self, data_test: str):
        # Buscar elemento por data-test ids
        return self.web.find_elements(By.CSS_SELECTOR, f"[data-test={data_test}]")

    def bySelector(self, element: str):
        # Buscar elemento por selector CSS
        return self.web.find_element(By.CSS_SELECTOR, element)

    def bySelectors(self, element: str):
        # Buscar elemento por selector CSS
        return self.web.find_elements(By.CSS_SELECTOR, element)

    def byTag(self, element: str):
        # Buscar elemento por nombre de etiqueta
        return self.web.find_element(By.TAG_NAME, element)

    def byTags(self, element: str):
        # Buscar elemento por nombre de etiqueta
        return self.web.find_elements(By.TAG_NAME, element)

    def byID(self, element: str):
        # Buscar elemento por ID
        return self.web.find_element(By.ID, element)

    def byIDs(self, element: str):
        # Buscar elemento por ID
        return self.web.find_elements(By.ID, element)

    def byClass(self, element: str):
        # Buscar elemento por nombre de clase
        return self.web.find_element(By.CLASS_NAME, element)

    def byClasses(self, element: str):
        # Buscar elemento por nombre de clase
        return self.web.find_elements(By.CLASS_NAME, element)

    def byName(self, element: str):
        # Buscar elemento por nombre
        return self.web.find_element(By.NAME, element)

    def byNames(self, element: str):
        # Buscar elemento por nombre
        return self.web.find_elements(By.NAME, element)

    def byXpath(self, element: str):
        # Buscar elemento por XPath
        return self.web.find_element(By.XPATH, element)

    def byXpaths(self, element: str):
        # Buscar elemento por XPath
        return self.web.find_elements(By.XPATH, element)

    # * ---- Smart Locators

    def containsAll(self, text: str):
        # Buscar todos los elementos que contengan dado innerText como contenedor (no estricto)
        return self.web.find_elements(By.XPATH, f'//*[contains(text(),"{text}")]')

    def contains(self, text: str):
        # Buscar el primer elemento único que contenga dado innerText como contenedor (no estricto)
        return self.web.find_element(By.XPATH, f'//*[contains(text(),"{text}")]')

    def withinElement_get(self, parentElement: WebElement, childElement: str):
        # Buscar un element específico dentro de un elemento padre
        return parentElement.find_element(By.CSS_SELECTOR, childElement)

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
                EC.presence_of_element_located(
                    (By.XPATH, f'//*[contains(text(),"{text}")]'))
            )
            return True
        except TimeoutException:
            return False

    def wait_until_element_clickable(self, text: str, timeout=10):
        # Esperar hasta que se pueda hacer click al elemento
        WebDriverWait(self.web, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, f'//*[contains(text(),"{text}")]'))
        )

    def scroll_down_200pixels(self):
        self.web.execute_script("window.scrollBy(0, {})".format(200))

    def scroll_down_300pixels(self):
        self.web.execute_script("window.scrollBy(0, {})".format(300))

    def scroll_down_400pixels(self):
        self.web.execute_script("window.scrollBy(0, {})".format(400))

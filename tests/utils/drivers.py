# -----
# * aquí se instancia todos los WebDrivers que se necesiten
import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOpt
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOpt
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOpt
from webdriver_manager.firefox import GeckoDriverManager

# Obtener la ruta absoluta del archivo actual
__filename = os.path.abspath(__file__)

# Navegar hacia atrás hasta la raíz del repositorio
__rootdir = os.path.join(os.path.dirname(__filename), '..', '..')

# Normalizar la ruta para resolver cualquier '..'
__rootdir = os.path.normpath(__rootdir)

# Combinar la ruta de la raíz del repositorio con el directorio específico
path_to_extension = os.path.join(
    __rootdir, 'extension/adblock.crx')


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        "--headless", action="store", default="false",
        help="Test execution in headless: true or false",
        choices=("true", "false"),
    )


@pytest.fixture
def headless(request: pytest.FixtureRequest):
    return request.config.getoption("--headless")


class Drivers:

    def __init__(self, isHeadless=False) -> None:
        self.isHeadless = isHeadless

    def chromeDriver(self):
        # *  Se crea una instancia del Chrome
        execution = ChromeOpt()
        if self.isHeadless == True:
            fileExists = os.path.exists(path_to_extension)
            if not fileExists:
                raise FileNotFoundError("The specified file does not exist.")
            execution.add_argument("--headless")
            execution.add_extension(path_to_extension)
            chrome = webdriver.Chrome(service=ChromiumService(
                ChromeDriverManager().install()), options=execution)
            original_window = chrome.current_window_handle
            windows = chrome.window_handles
            chrome.switch_to.window(windows[1])
            chrome.close()
            chrome.switch_to.window(original_window)
            return chrome
        else:
            fileExists = os.path.exists(path_to_extension)
            if not fileExists:
                raise FileNotFoundError("The specified file does not exist.")
            execution.add_extension(path_to_extension)
            chrome = webdriver.Chrome(service=ChromiumService(
                ChromeDriverManager().install()), options=execution)
            original_window = chrome.current_window_handle
            windows = chrome.window_handles
            chrome.switch_to.window(windows[1])
            chrome.close()
            chrome.switch_to.window(original_window)
            return chrome

    def edgeDriver(self):
        # *  Se crea una instancia del Microsoft Edge
        if self.isHeadless == True:
            execution = EdgeOpt()
            execution.add_argument("--headless")
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=execution)
        else:
            return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def firefoxDriver(self):
        # *  Se crea una instancia del FireFox
        if self.isHeadless == True:
            execution = FirefoxOpt()
            execution.add_argument("--headless")
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=execution)
        else:
            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


if __name__ == "__main__":
    pytest.main()

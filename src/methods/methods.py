
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException



class Methods():
    """
    Класс содержит БАЗОВЫЕ методы
    """
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(lambda driver: driver.find_element(*locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за {time} секунд")
            return None

    def find_elements(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(*locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за {time} секунд")
            return None
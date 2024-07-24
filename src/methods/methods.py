from selenium.webdriver import ActionChains
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

    def swipe_banner(self, banner_locator):
        if self.find_element(banner_locator):
            action = ActionChains(self.driver)
            element = self.find_element(banner_locator)

            # # Пример действия: клик по элементу
            # action.click(element).perform()

            # Пример действия: свайп
            action.drag_and_drop_by_offset(element, 0, 300).perform()

from appium.webdriver.common.appiumby import AppiumBy
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

    def  check_browser(self):
        """
        Закрываем окно проверки пробузера. Локатор разместил тут, т.к. метод универсальный
        """
        LOCATOR_CLOSE_CHECK_BROWSER = (AppiumBy.ID, 'ru.ozon.app.android:id/closeButtonImageView')

        self.find_element(LOCATOR_CLOSE_CHECK_BROWSER)

    def push_button_remind_me_later(self):
        """
        Закрываем предложение об уведомлениях. Локатор разместил тут, т.к. метод универсальный
        """
        LOCATOR_REMIND_MY_LETTER_BUTTON = (AppiumBy.XPATH,
           '//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/remindLater"]/android.view.View[1]')

        button_remind_later = self.find_element(LOCATOR_REMIND_MY_LETTER_BUTTON)
        button_remind_later.click()

    def swipe_banner(self):
        """
        Закрываем рекламный баннер свайпом вниз. Локатор разместил тут, т.к. метод универсальный
        """
        SWIPE_BANNER_DOWN_LOCATOR = (AppiumBy.ID, 'ru.ozon.app.android:id/sheetDialogTongue')

        if self.find_element(SWIPE_BANNER_DOWN_LOCATOR):
            action = ActionChains(self.driver)
            element = self.find_element(SWIPE_BANNER_DOWN_LOCATOR)

            # # Пример действия: клик по элементу
            # action.click(element).perform()

            # Пример действия: свайп
            action.drag_and_drop_by_offset(element, 0, 300).perform()

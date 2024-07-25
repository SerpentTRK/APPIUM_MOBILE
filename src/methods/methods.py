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

    def find_element(self, locator, time=2):
        try:
            return WebDriverWait(self.driver, time).until(lambda driver: driver.find_element(*locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за {time} секунд")
            return None

    def find_elements(self, locator, time=2):
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(*locator))
        except TimeoutException:
            print(f"Элемент с локатором {locator} не был найден за {time} секунд")
            return None

    def check_browser(self):
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

    def swipe_down(self, repeat_n_times=1):
        """
        Скроллим страницу вниз

         start_y = берем 80% высоты экрана и используем это значение как начальную точку y для свайпа вниз
         end_y = 20% высоты экрана и используется как конечная точка y для свайпа
         start_x = мы берем половину ширины экрана и используем это значение как x координату для свайпа. Таким образом,
        свайп будет происходить по центру экрана по горизонтали.
        """
        size = self.driver.get_window_size()

        start_y = size['height'] * 0.8  # 1929
        end_y = size['height'] * 0.2  # 482
        start_x = size['width'] / 2

        for each in range(1, repeat_n_times):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def swipe_up(self, repeat_n_times=1):
        """
        Скроллим страницу вверх

         start_y = берем 80% высоты экрана и используем это значение как начальную точку y для свайпа вниз
         end_y = 20% высоты экрана и используется как конечная точка y для свайпа
         start_x = мы берем половину ширины экрана и используем это значение как x координату для свайпа. Таким образом,
        свайп будет происходить по центру экрана по горизонтали.
        """
        size = self.driver.get_window_size()

        print(size['height'], size['height'] * 0.2, size['height'] * 0.8)
        start_y = size['height'] * 0.2 # 482
        end_y = size['height'] * 0.8  # 1929
        start_x = size['width'] / 2

        for each in range(1, repeat_n_times):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)

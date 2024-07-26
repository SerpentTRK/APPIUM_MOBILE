import base64
import os
import io
import cv2
import time

from pytest_check import check
import numpy as np
from PIL import Image
from io import BytesIO


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
        if button_remind_later is not None:
            button_remind_later.click()
        else:
            print('Handle the case when element is not found')


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
        """
        size = self.driver.get_window_size()

        start_y = size['height'] * 0.2 # 482
        end_y = size['height'] * 0.8  # 1929
        start_x = size['width'] / 2

        for each in range(1, repeat_n_times):
            self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def swipe_right(self, repeat_n_times=1):
        """
        Скроллим страницу вправо
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.2
        end_x = size['width'] * 0.8
        start_y = size['height'] / 2

        for each in range(1, repeat_n_times):
            self.driver.swipe(start_x, start_y, end_x, start_y, 800)

    def swipe_left(self, repeat_n_times=1):
        """
        Скроллим страницу влево
        """
        size = self.driver.get_window_size()
        start_x = size['width'] * 0.8
        end_x = size['width'] * 0.2
        start_y = size['height'] / 2

        for each in range(1, repeat_n_times):
            self.driver.swipe(start_x, start_y, end_x, start_y, 800)

    def take_screenshot(self, folder, filename):
        """
        Для валидации интерфейса нам нужно делать скриншоты
        """
        screenshot = self.driver.get_screenshot_as_base64()
        screen_image = Image.open(BytesIO(base64.b64decode(screenshot)))

        # Отрезание верхних 50 пикселей
        cropped_image = screen_image.crop((0, 150, screen_image.width, screen_image.height))

        filepath = os.path.join(folder, filename)
        cropped_image.save(filepath)  # Сохранение отрезанного скриншота

    def compare_interface_with_screen(self, interface_image_name, threshold=0.05):
        """
        Сравнение обрезанного скриншота с изображением интерфейса
        нужен импорт import cv2. установка библиотека OpenCV и numpy
        """
        # Получение снимка экрана
        screenshot = self.driver.get_screenshot_as_png()
        screenshot_image = Image.open(io.BytesIO(screenshot))
        # Обрезка верхней части скриншота на 150 пикселей
        screenshot_cropped = screenshot_image.crop((0, 150, screenshot_image.width, screenshot_image.height))

        # Путь к изображению интерфейса
        interface_image_path = '..\\resources\\' + interface_image_name
        # Загрузка изображения интерфейса
        interface_image = Image.open(interface_image_path)

        # Преобразование изображений в массивы numpy
        screenshot_array = np.array(screenshot_cropped)
        interface_array = np.array(interface_image)

        # Вычисление различий между изображениями
        difference = cv2.absdiff(screenshot_array, interface_array)
        diff_percentage = (np.count_nonzero(difference) / screenshot_array.size)

        check.less_equal(diff_percentage, threshold, msg=f"Ошибка! Скриншот отличается от эталонного изображения {interface_image_name} более чем на {threshold}%")

        # Сравнение с порогом несовпадения. Пока оставим
        if diff_percentage <= threshold:
            print(f"Изображения почти идентичны. Различия составляют {diff_percentage}%")
        else:
            print("Изображения различаются.")

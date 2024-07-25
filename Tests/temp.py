import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

from src.data_for_tests.open_ozon_application_testdata import OzonAppLocators
from src.methods.methods import Methods

check_browser_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/closeButtonImageView')
button_remind_later_locator = (AppiumBy.XPATH,
       '//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/remindLater"]/android.view.View[1]')
swipe_banner_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/sheetDialogTongue')

user_accaunt_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[6]')
user_cart_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[5]')
ozon_bank_card_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[4]')
exit_button_locator = (AppiumBy.XPATH, '//android.widget.ImageButton')
fashion_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[3]')
kill_fashion_reclam_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/closeSIB')
fashion_men_locator = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="tab_2"]')

exit_from_section_locator = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="zeroRight0"]/android.view.View')

ozon_fresh_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[2]')


class OpenOzonApplication(Methods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def run_test(self):
        self.check_browser()
        self.push_button_remind_me_later()
        self.swipe_banner(swipe_banner_locator)
        self.user_accaunt()
        self.user_cart()
        self.ozon_bank_card()
        self.ozon_fashion()
        self.ozon_fresh()

        time.sleep(5)


    def  check_browser(self):
        self.find_element(OzonAppLocators.LOCATOR_CLOSE_CHECK_BROWSER)

    def push_button_remind_me_later(self):
        button_remind_later = self.find_element(button_remind_later_locator)
        button_remind_later.click()

    def user_accaunt(self):
        my_accaun = self.find_element(user_accaunt_locator)
        my_accaun.click()

        self.driver.press_keycode(4)  # -> BACK

    def user_cart(self):
        my_cart = self.find_element(user_cart_locator)
        my_cart.click()

        self.driver.press_keycode(4)  # -> BACK

    def ozon_bank_card(self):
        bank_card = self.find_element(ozon_bank_card_locator)
        bank_card.click()

        time.sleep(10)                # долго открывается страница

        exit_button = self.find_element(exit_button_locator)
        exit_button.click()

    def ozon_fashion(self):
        fashion = self.find_element(fashion_locator)
        fashion.click()

        time.sleep(1)

        if self.find_element(kill_fashion_reclam_locator):
            kill_fashion_reclam = self.find_element(kill_fashion_reclam_locator)
            kill_fashion_reclam.click()

        man_fashion = self.find_element(fashion_men_locator)
        man_fashion.click()

        time.sleep(3)

        exit_fashion = self.find_element(exit_from_section_locator)
        exit_fashion.click()

    def ozon_fresh(self):
        ozon_fresh = self.find_element(ozon_fresh_locator)
        ozon_fresh.click()

        self.swipe_banner(swipe_banner_locator)

        exit_fresh = self.find_element(exit_from_section_locator)
        exit_fresh.click()

"""
 b. adb devices
 c. adb shell
 d. dumpsys window displays | grep -E 'mCurrentFocus'
 e. dumpsys window displays | grep -E 'mFocusedApp'
 
 adb shell dumpsys window | find "mCurrentFocus"
"""

"""
Порядок действий

Чтобы зайти в приложение, например Камера. Порядок действий:
- В телефон включена отладка по USB и Отключен контроль разрешений (перезагрузили)
- Подключили к компьютеру, выбрали что-то адндроид, передача файлов
- Зашли в андроид студио и запустили "adb devices" в терминале. Получили имя устройства, и вообще убедились, что подключены
- Запускаем appium
- Подключаемся через аппиум инспектор. На входе: 
        {
          "platformName": "Android",
          "appium:automationName": "uiautomator2",
          "appium:platformVersion": "13",
          "appium:deviceName": "5D894HG6GMZXWK4L",
        }
- Открываем на телефоне нужное нам приложение
- Идем в андроид студио, и вводим команды:
    adb shell
    dumpsys window displays | grep -E 'mCurrentFocus'
    В ответе первая часть это appPackage, а вторая appActivity
- Закрываем сессию в аппиум инспекторе, и добиваем данные для подключения атрибутами нашего приложения:
        {
          "platformName": "Android",
          "appium:automationName": "uiautomator2",
          "appium:platformVersion": "13",
          "appium:deviceName": "5D894HG6GMZXWK4L",
          "appium:appPackage": "com.oplus.camera",
          "appium:appActivity": "com.oplus.camera.Camera"
        }
    Теперь при запуске аппиум инспектора у нас сразу откроется нужное нам приложение
    
    Просто команды, которые я нарыл:
    - Эта команда предоставляет приложению с пакетным именем com.arlosoft.macrodroid разрешение 
    android.permission.CHANGE_CONFIGURATION через adb shell:
        adb shell pm grant com.arlosoft.macrodroid android.permission.CHANGE_CONFIGURATION
    - Эта команда предоставляет приложению с пакетным именем com.arlosoft.macrodroid разрешение 
    android.permission.WRITE_SECURE_SETTINGS через adb shell:
        adb shell pm grant com.arlosoft.macrodroid android.permission.WRITE_SECURE_SETTINGS
"""


## Это образец работающего теста, где все на одной странице. Начало

import time

import pytest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.action_chains import ActionChains




capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.oplus.camera',
    appActivity='com.oplus.camera.Camera',
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'


@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
    yield app_driver
    if app_driver:
        app_driver.quit()


def test_find_battery(driver):
    el = driver.find_element(AppiumBy.ID, "com.oplus.camera:id/btn_confirm")
    el.click()

    driver.find_element(AppiumBy.ID, '00000000-0000-026d-ffff-ffff00000052')

    driver.press_keycode()

    time.sleep(3)

## Это образец работающего теста, где все на одной странице. Конец

"""
self.driver.press_keycode(4)  # -> BACK, 3 - HOME

Для навигации на экран с открытыми приложениями в Appium обычно используется команда 
driver.pressKey(new KeyEvent(AndroidKey.APP_SWITCH));. 
Чтобы нажать кнопку "Квадратик", можно использовать команду driver.pressKey(new KeyEvent(AndroidKey.HOME));. 
Для нажатия на кнопку "стрелочка" можно воспользоваться командой driver.pressKey(new KeyEvent(AndroidKey.BACK));.
"""


## Сравнение изображений
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# import base64
#
# # Получение скриншотов
# screenshot1 = base64.b64encode(driver.get_screenshot_as_png())
# screenshot2 = base64.b64encode(driver.get_screenshot_as_png())
#
# # Сравнение скриншотов
# result = driver.get_images_similarity(screenshot1, screenshot2, SimilarityMatchingOptions().with_enabled_visualization())
# assert len(result.visualization) > 0
# assert result.score > 0.0
# ##


# # Импорт необходимых модулей
# from PIL import Image
# from io import BytesIO
# from appium import images
#
#     # Создание скриншота экрана с отрезанными верхними 50 пикселями и сохранение на диск
#     def take_and_save_screenshot_without_top_region(self, top_region_height, save_path):
#         # Получение скриншота экрана
#         screenshot = self.driver.get_screenshot_as_base64()
#         screen_image = Image.open(BytesIO(base64.b64decode(screenshot)))
#
#         # Отрезание верхних 50 пикселей
#         screen_width, screen_height = screen_image.size
#         cropped_image = screen_image.crop((0, top_region_height, screen_width, screen_height))
#
#         # Сохранение отрезанного скриншота
#         cropped_image.save(save_path)
#
#         return cropped_image
#
#
#
#     # Загрузка изображения интерфейса и сравнение с определенной областью изображения на экране за исключением верхних 50 пикселей
#     def compare_screen_without_top_region(self, interface_image_path, top_region_height):
#         # Загрузка изображения интерфейса
#         interface_image = Image.open(interface_image_path)
#
#         # Получение скриншота экрана
#         screenshot = driver.get_screenshot_as_base64()
#         screen_image = Image.open(BytesIO(base64.b64decode(screenshot)))
#
#         # Определение и выделение области на скриншоте без верхних 50 пикселей
#         screen_width, screen_height = screen_image.size
#         region = screen_image.crop((0, top_region_height, screen_width, screen_height))
#
#         # Сравнение изображения интерфейса с областью на экране без верхних 50 пикселей
#         comparison_result = images.compare_images_from_pil_images(region, interface_image)
#
#         if comparison_result["result"]:
#             print("Изображения в указанной области идентичны.")
#         else:
#             print(
#                 "Изображения в указанной области различаются. Различия: {}".format(comparison_result["diff_image_base64"]))
#
#
#     # Пример использования
#     compare_screen_without_top_region(driver, "expected_interface.png", top_region_height=50)
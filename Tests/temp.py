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
"""
Installation плагин images для сравнения изображений
appium plugin install images
The plugin must be explicitly activated when launching the Appium server:

appium --use-plugins=images
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
## рабочий тест для формирования скриншотов. Этот метод вызывает базовый метод в Methods. Нужно только менять
# имена сохраняемых файлов
import os
def take_and_save_screenshot(self):
    folder_path = os.path.join(os.getcwd(), "save_screenshot")  # Получаем путь к папке save_screenshot внутри проекта
    self.take_screenshot(folder_path, "screenshot_system color.png")

###########################################

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

"""
        # Кликнуть в точку на экране по заданным координатам (x, y)
        self.driver.tap([(14, 1714)])

        # Выполнить свайп вправо на 400 пикселей
        start_x = 14
        start_y = 1714
        end_x = start_x + 400
        end_y = start_y
        self.driver.swipe(start_x, start_y, end_x, end_y, 800)
"""

"""
#Поиск по изображению

from appium import webdriver
from PIL import Image
import io
import base64

# Создание экземпляра драйвера Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", {
    "platformName": "Android",
    "deviceName": "emulator",
    "appPackage": "com.example.myapp",
    "appActivity": "com.example.myapp.MainActivity"
})

# Загрузка образца изображения
with open("template.png", "rb") as f:
    template_image = Image.open(f)
    template_image_bytes = io.BytesIO()
    template_image.save(template_image_bytes, format="PNG")
    template_image_bytes.seek(0)
    template_image_base64 = base64.b64encode(template_image_bytes.read()).decode()

# Поиск элемента на основе образца
element = driver.find_element("-image", template_image_base64)
"""


"""
# В Appium вы можете использовать метод find_element для поиска элементов на основе их образца. Вот пример кода на 
# Python, который ищет элемент на основе образца изображения:

from appium import webdriver
from PIL import Image
import io
import base64

# Создание экземпляра драйвера Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", {
    "platformName": "Android",
    "deviceName": "emulator",
    "appPackage": "com.example.myapp",
    "appActivity": "com.example.myapp.MainActivity"
})

# Загрузка образца изображения
with open("template.png", "rb") as f:
    template_image = Image.open(f)
    template_image_bytes = io.BytesIO()
    template_image.save(template_image_bytes, format="PNG")
    template_image_bytes.seek(0)
    template_image_base64 = base64.b64encode(template_image_bytes.read()).decode()

# Поиск элемента на основе образца
element = driver.find_element("-image", template_image_base64)
"""

"""
# Если у вас есть более сложные требования к приближению, вы можете использовать метод pinch для 
выполнения более детального управления приближением. Вот пример кода, который демонстрирует, как 
использовать метод pinch для приближения элемента:

from appium import webdriver

# Создание экземпляра драйвера Appium
driver = webdriver.Remote("http://localhost:4723/wd/hub", {
    "platformName": "Android",
    "deviceName": "emulator",
    "appPackage": "com.example.myapp",
    "appActivity": "com.example.myapp.MainActivity"
})

# Поиск элемента
element = driver.find_element_by_accessibility_id("my_element")

# Получение координат центра элемента
center_x = element.size['width'] / 2 + element.location['x']
center_y = element.size['height'] / 2 + element.location['y']

# Приближение элемента
driver.pinch(element, percent=20, center_x=center_x, center_y=center_y)
"""
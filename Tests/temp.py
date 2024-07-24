
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
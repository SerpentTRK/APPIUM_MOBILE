"""
Всякие тесты

Для запуска Appium-локатора:
{
  "platformName": "Android",
  "automationName": "uiautomator2"
}

1. Заходим в Андроид студию, в тестовый проект. Открываем терминал
В терминале вводим:
1. adb shell
2. dumpsys window displays | grep -E 'mCurrentFocus'
В ответе первая часть это appPackage, а вторая appActivity

"""
"""
 b. adb devices
 c. adb shell
 d. dumpsys window displays | grep -E 'mCurrentFocus'
 e. dumpsys window displays | grep -E 'mFocusedApp'
 
 adb shell dumpsys window | find "mCurrentFocus"
"""









## Это изначальный первый тест. Начало
import time

import pytest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
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
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

    time.sleep(3)

## Это изначальный первый тест. Конец


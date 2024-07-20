import time

import pytest

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

# - automationName: UiAutomator2
# - platformNames: ["Android"]

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

# def tearDown(self) -> None:
#     if self.driver:
#         self.driver.quit()

def test_find_battery(driver):
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()

    time.sleep(3)
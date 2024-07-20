
import pytest

from appium import webdriver
from appium.options.android import UiAutomator2Options



@pytest.fixture
def driver():
    """
    Фикстура создает содеинение с нужным нам элементом интерфейса
    """
    android_driver = None
    def _wrapped(appPackage, appActivity):
        nonlocal android_driver

        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            appPackage=appPackage,
            appActivity=appActivity,
            language='en',
            locale='US'
        )

        capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
        appium_server_url = 'http://localhost:4723'

        android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)

        return android_driver
    yield _wrapped

    if android_driver:
        android_driver.quit()

import pytest

from appium import webdriver
from src.utils.appium_utils import appium_server_url, capabilities_options


@pytest.fixture()
def driver():
    """
    Инициализация драйвера Appium
    """
    android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)

    yield android_driver

    android_driver.quit()




# @pytest.fixture
# def driver():
#     """
#     Инициализация драйвера Appium
#     """
#     android_driver = None
#     def _wrapped(appPackage, appActivity):
#         nonlocal android_driver
#
#         capabilities = dict(
#             platformName='Android',
#             automationName='uiautomator2',
#             deviceName='Android',
#             appPackage=appPackage,
#             appActivity=appActivity,
#             language='en',
#             locale='US'
#         )
#
#         capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
#         appium_server_url = 'http://localhost:4723'
#
#         android_driver = webdriver.Remote(appium_server_url, options=capabilities_options)
#
#         return android_driver
#     yield _wrapped
#
#     android_driver.quit()
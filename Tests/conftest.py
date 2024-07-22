
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


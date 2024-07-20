
import time

from appium.webdriver.common.appiumby import AppiumBy

from src.test_workspase.test_click_camera_icon import ClickCameraIcon
from src.test_workspase.test_find_battery import TestFindBattery




def test_find_battery(driver):
    appPackage = 'com.android.settings'
    appActivity = '.Settings'

    element = TestFindBattery(driver(appPackage, appActivity))
    element.start_test()


def test_click_camera_icon_02(driver):

    appPackage = 'com.google.android.apps.nexuslauncher'
    appActivity = 'android.widget.TextView'

    element = ClickCameraIcon(driver(appPackage, appActivity))
    element.start_test()

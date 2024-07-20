import time

from appium.webdriver.common.appiumby import AppiumBy

class TestFindBattery():
    def __init__(self, driver):
        self.driver = driver

    def start_test(self):
        element = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        element.click()

        time.sleep(3)
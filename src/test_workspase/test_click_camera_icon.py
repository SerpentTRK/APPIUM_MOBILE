import time

from appium.webdriver.common.appiumby import AppiumBy

class ClickCameraIcon():
    def __init__(self, driver):
        self.driver = driver

    def start_test(self):

        button_confirm = self.driver.find_element(AppiumBy.ID, "com.oplus.camera:id/btn_confirm")
        button_confirm.click()

        time.sleep(3)



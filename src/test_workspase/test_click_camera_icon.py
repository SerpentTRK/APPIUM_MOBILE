import time

from appium.webdriver.common.appiumby import AppiumBy

class ClickCameraIcon():
    def __init__(self, driver):
        self.driver = driver

    def start_test(self):


        camera_icon = self.driver.find_element(by=AppiumBy.XPATH,
           value='//android.widget.Button[@resource-id="com.google.android.apps.photos:id/onboarding_action_button"]')
        camera_icon.click()

        time.sleep(3)



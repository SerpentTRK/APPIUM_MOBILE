import time

from appium.webdriver.common.appiumby import AppiumBy

class Camera():
    def __init__(self, driver):
        self.driver = driver

    def run_test(self):
        self.confirm_button()
        self.flashlight()

    def confirm_button(self):
        button_confirm = self.driver.find_element(AppiumBy.ID, "com.oplus.camera:id/btn_confirm")
        button_confirm.click()

    def flashlight(self):
        flash_menu = self.driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="FlashOff"]')
        flash_menu.click()

        choice_auto = self.driver.find_element(AppiumBy.XPATH,
                   '//android.widget.RelativeLayout[@resource-id="com.oplus.camera:'
                   'id/camera_setting_layout_second_level"]/android.widget.ImageView[3]')
        choice_auto.click()

        time.sleep(3)




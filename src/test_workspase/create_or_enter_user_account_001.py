import base64
import time
import os

from src.data_for_tests.create_or_enter_user_account_001_testdata import UserAccountLocators
from src.methods.methods import Methods


class CreateOrEnterUserAccount(Methods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def run_test(self):
        self.check_browser()
        self.push_button_remind_me_later()
        self.swipe_banner()
        self.user_accaunt()
        self.swipe_down(2)
        self.swipe_up(3)
        time.sleep(1)
        self.take_and_save_screenshot()




        self.driver.press_keycode(4)  # -> BACK
        time.sleep(0.5)

    def user_accaunt(self):
        my_accaunt = self.find_element(UserAccountLocators.LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT)
        my_accaunt.click()

    def change_app_color(self):
        app_color = self.find_element(UserAccountLocators.LOCATOR_COLOR_APP)
        app_color.click()

    def take_and_save_screenshot(self):
        folder_path = os.path.join(os.getcwd(), "resources")  # Получаем путь к папке resources внутри проекта
        self.take_screenshot(folder_path, "screenshot_system color.png")





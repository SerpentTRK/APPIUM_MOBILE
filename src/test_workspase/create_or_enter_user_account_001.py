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
        self.change_app_color()
        time.sleep(3)
        self.swipe_down(4)
        self.swipe_up(4)

        self.driver.press_keycode(4)  # -> BACK
        time.sleep(1)

        # self.take_and_save_screenshot()
        # self.compare_interface_with_screen("screenshot_app_system_color.png")

    def user_accaunt(self):
        my_accaunt = self.find_element(UserAccountLocators.LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT)
        my_accaunt.click()

    def take_and_save_screenshot(self, file_name):
        folder_path = os.path.join(os.getcwd(), "save_screenshot")  # Получаем путь к папке save_screenshot внутри проекта
        self.take_screenshot(folder_path, file_name)

    def change_app_color(self):
        app_color = self.find_element(UserAccountLocators.LOCATOR_COLOR_APP)
        app_color.click()
        choice_dark_theme = self.find_element(UserAccountLocators.LOCATOR_DARK_THEME)
        choice_dark_theme.click()
        self.compare_interface_with_screen("screenshot_app_dark_theme.png")
        choice_system_theme = self.find_element(UserAccountLocators.LOCATOR_SYSTEM_THEME)
        choice_system_theme.click()
        self.compare_interface_with_screen("screenshot_app_system_color.png")

        self.driver.press_keycode(4)  # -> BACK








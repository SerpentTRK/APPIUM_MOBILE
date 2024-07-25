
import time

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
        self.swipe_down(5)
        self.swipe_up(5)


        self.driver.press_keycode(4)  # -> BACK
        time.sleep(0.5)

    def user_accaunt(self):
        my_accaunt = self.find_element(UserAccountLocators.LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT)
        my_accaunt.click()

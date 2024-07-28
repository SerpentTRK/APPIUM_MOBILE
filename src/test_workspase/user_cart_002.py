
import time
import os

from src.data_for_tests.user_cart_002_testdata import UserCartLocators
from src.methods.methods import Methods


class UserCart(Methods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def run_test(self):
        self.check_browser()
        self.push_button_remind_me_later()
        self.swipe_banner()
        self.user_cart()
        self.choice_destination()

        self.driver.press_keycode(4)  # -> BACK
        time.sleep(1)

    def user_cart(self):
        my_cart = self.find_element(UserCartLocators.LOCATOR_USER_CART)
        my_cart.click()

        time.sleep(3)

    def choice_destination(self):
        arrow = self.find_element(UserCartLocators.LOCATOR_ARROW)
        arrow.click()

        if not self.find_element(UserCartLocators.LOCATOR_ADD_ADDRESS):
            old_pvz = self.find_element(UserCartLocators.LOCATOR_OLD_PVZ)
            old_pvz.click()
            del_pvz = self.find_element(UserCartLocators.LOCATOR_DEL_PVZ)
            del_pvz.click()
            confirm = self.find_element(UserCartLocators.LOCATOR_DEL_CONFIRM)
            confirm.click()

            add_address = self.find_element(UserCartLocators.LOCATOR_ADD_ADDRESS)
            add_address.click()

            dont_allow_button = self.find_element(UserCartLocators.LOCATOR_DONT_ALLOW_LOCATION)
            dont_allow_button.click()

            seapch_pvz = self.find_element(UserCartLocators.LOCATOR_SEARC_PVZ)
            seapch_pvz.click()

            get_pvz = self.find_element(UserCartLocators.LOCATOR_TEXT_INPUT)
            get_pvz.send_keys("курочкина 5")

            choise_pvz = self.find_element(UserCartLocators.LOCATOR_CHOICE_PVZ)
            choise_pvz.click()

            my_pvz = self.find_element(UserCartLocators.LOCATOR_MY_PVZ)
            my_pvz.click()

        else:
            add_address = self.find_element(UserCartLocators.LOCATOR_ADD_ADDRESS)
            add_address.click()

            dont_allow_button = self.find_element(UserCartLocators.LOCATOR_DONT_ALLOW_LOCATION)
            dont_allow_button.click()

            map = self.find_element(UserCartLocators.LOCATOR_MAP)
            map.click()

            self.choice_point_in_screen(14, 1709)

            seapch_pvz = self.find_element(UserCartLocators.LOCATOR_SEARC_PVZ)
            seapch_pvz.click()

            get_pvz = self.find_element(UserCartLocators.LOCATOR_TEXT_INPUT)
            get_pvz.send_keys("курочкина 5")

            choise_pvz = self.find_element(UserCartLocators.LOCATOR_CHOICE_PVZ)
            choise_pvz.click()

            my_pvz = self.find_element(UserCartLocators.LOCATOR_MY_PVZ)
            my_pvz.click()

        address_pvz = self.find_element(UserCartLocators.LOCATOR_ADDRESS_VALIDATION).text
        assert address_pvz == 'ул. Полковника Милиции Курочкина, 5'


    def take_and_save_screenshot(self, file_name):
        folder_path = os.path.join(os.getcwd(), "save_screenshot")  # Получаем путь к папке save_screenshot внутри проекта
        self.take_screenshot(folder_path, file_name)
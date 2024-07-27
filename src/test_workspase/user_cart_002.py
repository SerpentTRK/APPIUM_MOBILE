
import time
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.pointer_input import PointerInput

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

        time.sleep(3)





        # choice_town = self.find_element(UserCartLocators.LOCATOR_CHOICE_TOWN)
        # choice_town.click()
        #
        # get_town = self.find_element(UserCartLocators.LOCATOR_TEXT_INPUT)
        # get_town.send_keys("Троицк")
        #
        # choice_troitsk = self.find_element(UserCartLocators.LOCATOR_TROITSK)
        # choice_troitsk.click()
        #
        # troitsk_map = self.find_element(UserCartLocators.LOCATOR_MAP_OF_TROITSK)
        # troitsk_map.click()
        #
        # time.sleep(3)
        #
        # self.swipe_up()
        # self.swipe_right()
        #
        # time.sleep(3)


        ###
        # troitsk_map = self.find_element(UserCartLocators.LOCATOR_TROITSK_MAP)
        # troitsk_map.click()

        # actions = ActionChains(self.driver)
        # # override as 'touch' pointer action
        # actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        # actions.w3c_actions.pointer_action.move_to_location(500, 600)
        # actions.w3c_actions.pointer_action.pointer_down()
        # actions.w3c_actions.pointer_action.pause(2)
        # actions.w3c_actions.pointer_action.move_to_location(1230, 2315)
        # actions.w3c_actions.pointer_action.release()
        # actions.perform()

        # start_x = 500
        # start_y = 600
        # end_x = 1230
        # end_y = 2315
        # duration = 800
        #
        # touch_input = PointerInput(interaction.POINTER_TOUCH, 'touch')
        #
        # actions = ActionChains(self.driver)
        # actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input)
        # actions.w3c_actions.pointer_action.move_to_location(start_x, start_y)
        # actions.w3c_actions.pointer_action.pointer_down()
        # if duration > 0:
        #     actions.w3c_actions = ActionBuilder(self.driver, mouse=touch_input, duration=duration)
        # actions.w3c_actions.pointer_action.move_to_location(end_x, end_y)
        # actions.w3c_actions.pointer_action.release()
        # actions.perform()




    def take_and_save_screenshot(self, file_name):
        folder_path = os.path.join(os.getcwd(), "save_screenshot")  # Получаем путь к папке save_screenshot внутри проекта
        self.take_screenshot(folder_path, file_name)
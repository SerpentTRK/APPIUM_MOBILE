
import time

from src.data_for_tests.check_user_accaunt_001_testdata import UserAccountLocators
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
        self.swipe_down()
        self.swipe_up()

        time.sleep(5)
        self.driver.press_keycode(4)  # -> BACK



    def user_accaunt(self):
        my_accaun = self.find_element(UserAccountLocators.LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT)
        my_accaun.click()

    def swipe_down(self):
        size = self.driver.get_window_size()
        # берем 80% высоты экрана и используем это значение как начальную точку y для свайпа вниз
        start_y = size['height'] * 0.8
        # 20% высоты экрана и используется как конечная точка y для свайпа
        end_y = size['height'] * 2
        # мы берем половину ширины экрана и используем это значение как x координату для свайпа. Таким образом,
        # свайп будет происходить по центру экрана по горизонтали.
        start_x = size['width'] / 2
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)

    def swipe_up(self):
        size = self.driver.get_window_size()
        start_y = size['height'] * 2
        end_y = size['height'] * 0.8
        start_x = size['width'] / 2
        self.driver.swipe(start_x, start_y, start_x, end_y, 800)
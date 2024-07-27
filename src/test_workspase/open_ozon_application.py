
import time
import os

from src.methods.methods import Methods



class OpenOzonApplication(Methods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def run_test(self):
        self.check_browser()
        self.push_button_remind_me_later()
        self.swipe_banner()
        # из-за рандомных баннеров не реально валидировать страницу.
        # self.take_and_save_screenshot("main_screen.png")

    def take_and_save_screenshot(self, file_name):
        folder_path = os.path.join(os.getcwd(), "save_screenshot")  # Получаем путь к папке save_screenshot внутри проекта
        self.take_screenshot(folder_path, file_name)

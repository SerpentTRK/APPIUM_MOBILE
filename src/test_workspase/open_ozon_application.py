import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains

from src.methods.methods import Methods


check_browser_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/closeButtonImageView')
button_remind_later_locator = (AppiumBy.XPATH,
       '//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/remindLater"]/android.view.View[1]')
swipe_banner_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/sheetDialogTongue')

user_accaunt_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[6]')
user_cart_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[5]')
ozon_bank_card_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[4]')
exit_button_locator = (AppiumBy.XPATH, '//android.widget.ImageButton')
fashion_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[3]')
kill_fashion_reclam_locator = (AppiumBy.ID, 'ru.ozon.app.android:id/closeSIB')
fashion_men_locator = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="tab_2"]')

exit_from_section_locator = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="zeroRight0"]/android.view.View')

ozon_fresh_locator = (AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[2]')


class OpenOzonApplication(Methods):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

    def run_test(self):
        self.check_browser()
        self.push_button_remind_me_later()
        self.swipe_banner(swipe_banner_locator)
        self.user_accaunt()
        self.user_cart()
        self.ozon_bank_card()
        self.ozon_fashion()
        self.ozon_fresh()

        time.sleep(5)


    def  check_browser(self):
        self.find_element(check_browser_locator)

    def push_button_remind_me_later(self):
        button_remind_later = self.find_element(button_remind_later_locator)
        button_remind_later.click()

    def user_accaunt(self):
        my_accaun = self.find_element(user_accaunt_locator)
        my_accaun.click()

        self.driver.press_keycode(4)  # -> BACK

    def user_cart(self):
        my_cart = self.find_element(user_cart_locator)
        my_cart.click()

        self.driver.press_keycode(4)  # -> BACK

    def ozon_bank_card(self):
        bank_card = self.find_element(ozon_bank_card_locator)
        bank_card.click()

        time.sleep(10)                # долго открывается страница

        exit_button = self.find_element(exit_button_locator)
        exit_button.click()

    def ozon_fashion(self):
        fashion = self.find_element(fashion_locator)
        fashion.click()

        time.sleep(1)

        if self.find_element(kill_fashion_reclam_locator):
            kill_fashion_reclam = self.find_element(kill_fashion_reclam_locator)
            kill_fashion_reclam.click()

        man_fashion = self.find_element(fashion_men_locator)
        man_fashion.click()

        time.sleep(3)

        exit_fashion = self.find_element(exit_from_section_locator)
        exit_fashion.click()

    def ozon_fresh(self):
        ozon_fresh = self.find_element(ozon_fresh_locator)
        ozon_fresh.click()

        self.swipe_banner(swipe_banner_locator)

        exit_fresh = self.find_element(exit_from_section_locator)
        exit_fresh.click()








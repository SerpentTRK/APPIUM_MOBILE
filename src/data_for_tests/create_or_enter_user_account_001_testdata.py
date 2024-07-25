
from appium.webdriver.common.appiumby import AppiumBy



class UserAccountLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT = (AppiumBy.XPATH,
                '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[6]')




class UserAccountTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = ""
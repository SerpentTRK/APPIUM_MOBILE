
from appium.webdriver.common.appiumby import AppiumBy



class UserAccountLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_CREATE_OR_ENTER_USER_ACCAUNT = (AppiumBy.XPATH,
        '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[6]')
    LOCATOR_COLOR_APP = (AppiumBy.XPATH,
        '//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.ozon.app.android:id/listRv"]'
        '/android.widget.FrameLayout[2]/android.view.ViewGroup/android.view.View[5]')
    LOCATOR_DARK_THEME = (AppiumBy.ID, 'ru.ozon.app.android:id/darkV')
    LOCATOR_SYSTEM_THEME = (AppiumBy.ID, 'ru.ozon.app.android:id/inSystemV')
    LOCATOR_COLOR_APP_EXIT = (AppiumBy.ID, 'ru.ozon.app.android:id/collapsingTl')

class UserAccountTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = ""
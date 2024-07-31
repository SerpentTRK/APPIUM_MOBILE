
from appium.webdriver.common.appiumby import AppiumBy



class OzonAppLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_HORIZONTAL_LINE_WITH_ICON = (AppiumBy.XPATH,
        '(//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.ozon.app.android:id/itemsRv"])[2]')

class OzonAppTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = ""
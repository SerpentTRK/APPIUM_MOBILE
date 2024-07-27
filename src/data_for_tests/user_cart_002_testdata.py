
from appium.webdriver.common.appiumby import AppiumBy



class UserCartLocators:
    """
    Класс содержит локаторы для конкретной тестируемой страницы
    """
    LOCATOR_USER_CART = (AppiumBy.XPATH,
        '(//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/tab_icon"])[5]')
    LOCATOR_ARROW = (AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="disclosure"]')
    LOCATOR_ADD_ADDRESS = (AppiumBy.XPATH,
       '//android.widget.TextView[@resource-id="ru.ozon.app.android:id/titleTv" and @text="Добавить"]')
    LOCATOR_DONT_ALLOW_LOCATION = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button')
    LOCATOR_MAP = (AppiumBy.XPATH,
       '//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/containerLayout"]/android.view.ViewGroup')
    LOCATOR_SEARC_PVZ = (AppiumBy.XPATH,
        '//android.widget.FrameLayout[@resource-id="ru.ozon.app.android:id/searchButton"]')
    LOCATOR_TEXT_INPUT = (AppiumBy.ID, 'ru.ozon.app.android:id/fieldEt')
    LOCATOR_CHOICE_PVZ = (AppiumBy.XPATH,
        '//android.widget.TextView[@content-desc="улица Полковника Милиции Курочкина, 5, Троицк"]')
    LOCATOR_MY_PVZ = (AppiumBy.XPATH,
        '(//androidx.recyclerview.widget.RecyclerView[@resource-id="ru.ozon.app.android:id/listRv"])[2]')

    LOCATOR_OLD_PVZ = (AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="ru.ozon.app.android:id/buttonIv"]')
    LOCATOR_DEL_PVZ = (AppiumBy.ID, 'ru.ozon.app.android:id/popupTitleTv')
    LOCATOR_DEL_CONFIRM = (AppiumBy.ID, 'android:id/button1')

    LOCATOR_TROITSK_MAP = (AppiumBy.XPATH,
       '//android.view.ViewGroup[@resource-id="ru.ozon.app.android:id/containerLayout"]/android.view.ViewGroup')













class UserCartTestdata:
    """
    Класс содержит тестовые данные для конкретной тестируемой страницы
    """
    ALERT_CONFIRM_TEXT = ""

from appium.options.android import UiAutomator2Options

"""
Данные для инициализации драйвера Appium. 
"""

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='ru.ozon.app.android',                            # атрибут тестируемого приложения
    appActivity='ru.ozon.app.android.ui.start.AppHostActivity',  # атрибут тестируемого приложения
    # appPackage='com.oplus.camera',  # атрибут тестируемого приложения
    # appActivity='.Camera',          # атрибут тестируемого приложения
)

capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
appium_server_url = 'http://localhost:4723'

from src.test_workspase.open_ozon_application import OpenOzonApplication
from src.test_workspase.create_or_enter_user_account_001 import CreateOrEnterUserAccount
from src.test_workspase.user_cart_002 import UserCart


def test_open_ozon_application(driver):
    """
    Запуск приложения. Закрываем рекламный баннер, если он появляется.
    Свайпим центральную полоскуску с иконками различных сервисов
    """
    run_application = OpenOzonApplication(driver)
    run_application.run_test()


def test_create_or_enter_user_account_001(driver):
    """
    Раздел интерфейса для авторизации/регистрации в аккаунте пользователя. Регистрироваться мы не можем,
    т.к. и почистить тестовые данные мы тоже не можем. Посмотрим доступные настройки

    Проверить работу раздела "Цвет приложения". Изменить и вернуть цветовые темы,
    провалидировать изменение цветовых схем, проскроллить раздел вниз и вернуться наверх, выйти на главную страницу
    """
    user_accaunt = CreateOrEnterUserAccount(driver)
    user_accaunt.run_test()

def test_user_cart_002(driver):
    """
    Раздел интерфейса для доступа к корзине покупателя.

    Указать пункт самовывоза, отказаться от геолокации, выбрать город на карте, далее, т.к.
    точки ПВЗ то появляются, то нет, вбиваем часть имени улицы и дом. Находится нужный ПВЗ. Выбираем его.

    При повторном прогоне теста, когда ПВЗ уже выбран, сперва удаляется старый ПВЗ, а потом заводится новый.
    Валидация адреса доставки

    Из найденного. ГДе-то в корзине отображается адрес, без указания города
    (например в саомй корзине, если зайти с главного экрана), а если зайти из раздела fresh, то город, без улицы и дома.
    Если еду возят до адреса проживания, то на это можно и указать...
    """
    user_cart = UserCart(driver)
    user_cart.run_test()


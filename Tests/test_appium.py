from src.test_workspase.create_or_enter_user_account_001 import CreateOrEnterUserAccount
from src.test_workspase.open_ozon_application import OpenOzonApplication



def test_open_ozon_application(driver):
    """
    Запуск приложения. Закрываем рекламный баннер, если он появляется.
    Дальше пока не придумал.
    """
    run_application = OpenOzonApplication(driver)
    run_application.run_test()


def test_create_or_enter_user_account_001(driver):
    """
    Раздел интерфейса для авторизации/регистрации в аккаунте пользователя. Регистрироваться мы не можем,
    т.к. и почистить тестовые данные мы тоже не можем. Посмотрим доступные настройки

    Проверить работу раздела "Цвет приложения" и валюта. Изменить настроийки и вернуть их назад
    """
    user_accaunt = CreateOrEnterUserAccount(driver)
    user_accaunt.run_test()

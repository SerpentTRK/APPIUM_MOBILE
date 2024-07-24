
from src.test_workspase.open_ozon_application import OpenOzonApplication



def test_open_ozon_application(driver):
    application = OpenOzonApplication(driver)
    application.run_test()

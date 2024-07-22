
from src.test_workspase.test_camera import Camera



def test_camera(driver):
    element = Camera(driver)
    element.run_test()


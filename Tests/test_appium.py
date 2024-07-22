
from src.test_workspase.test_click_camera_icon import ClickCameraIcon



def test_click_camera_icon(driver):

    element = ClickCameraIcon(driver)
    element.start_test()


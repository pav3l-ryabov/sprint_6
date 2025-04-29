import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver_instance = webdriver.Firefox()
    driver_instance.set_window_size(1920, 1080)
    yield driver_instance
    driver_instance.quit()


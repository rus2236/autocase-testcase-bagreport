from selenium import webdriver
import pytest
from config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def init_driver():
    web_driver = webdriver.Chrome(executable_path=TestData.CHROME_DRIVER_PATH)
    web_driver.set_window_size(1400, 900)

    yield web_driver

    web_driver.quit()

import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def access_web():
    #前置
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")

    yield driver
    #后置
    time.sleep(2)
    driver.quit()
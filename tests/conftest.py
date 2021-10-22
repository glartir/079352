import time

import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    try:
        browser = webdriver.Chrome(executable_path="../chromedriver")
        browser.maximize_window()

        yield browser

    finally:
        time.sleep(5)
        browser.quit()

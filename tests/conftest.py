import pytest
from selenium import webdriver


@pytest.fixture
def browser():

    browser = webdriver.Chrome(executable_path="../chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()

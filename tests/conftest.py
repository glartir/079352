import pytest
from selenium import webdriver


@pytest.fixture
def browser():

    browser = webdriver.Chrome(executable_path="/home/viacheslav_sidorenko/PycharmProjects/079352/chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()

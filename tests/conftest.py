import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--start-maximized")  # open Browser in maximized mode
    options.add_argument("--no-sandbox")  # bypass OS security model
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options=options, executable_path="../chromedriver")
    # browser.maximize_window()
    yield browser
    browser.quit()

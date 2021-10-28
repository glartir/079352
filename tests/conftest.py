import pytest
from selenium import webdriver


@pytest.fixture
def browser():

    browser = webdriver.Chrome(executable_path="../chromedriver")
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_configure(config):
    config.addinivalue_line("markers", "high: marks high priority operation")
    config.addinivalue_line("markers", "low: marks low  priority operation")
    config.addinivalue_line("markers", "add: marks add operation")
    config.addinivalue_line("markers", "subtract: marks subtract operation")
    config.addinivalue_line("markers", "multiply: marks multiply operation")
    config.addinivalue_line("markers", "devide: marks devide operation")



def pytest_addoption(parser):
    parser.addoption('--first_arg', action='store', default=10)
    parser.addoption('--second_arg', action='store', default=20)
    parser.addoption('--result', action='store', default=200)


@pytest.fixture
def variables(request):
    x = float(request.config.getoption("first_arg"))
    y = float(request.config.getoption("second_arg"))
    value = float(request.config.getoption("result"))
    return x, y, value


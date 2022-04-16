import pytest
from selenium import webdriver
from users import REMOTE_CAPABILITIES
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def browser(request):
    driver_type = request.config.getoption("driver_type")
    if driver_type == "local":
        browser = webdriver.Chrome()
    elif driver_type == "remote":
        capabilities = REMOTE_CAPABILITIES

        browser = webdriver.Remote(
            command_executor="http://selenoid:4444/wd/hub", desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--driver_type should be local or remote")
    browser.maximize_window()
    yield browser
    if request.node.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)

    browser.quit()


def pytest_addoption(parser):
    parser.addoption('--driver_type', action='store', default='local',
                     help="Choose type of driver: local or remote")
    parser.addoption('--first_arg', action='store', default=10)
    parser.addoption('--second_arg', action='store', default=20)
    parser.addoption('--result', action='store', default=200)


@pytest.fixture
def variables(request):
    x = float(request.config.getoption("first_arg"))
    y = float(request.config.getoption("second_arg"))
    value = float(request.config.getoption("result"))
    return x, y, value


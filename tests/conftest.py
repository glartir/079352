import pytest
from selenium import webdriver
from users import REMOTE_CAPABILITIES
import allure


def pytest_addoption(parser):
    parser.addoption('--driver_type', action='store', default='local',
                     help="Choose type of driver: local or remote")


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
            command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
    else:
        raise pytest.UsageError("--driver_type should be local or remote")
    browser.maximize_window()
    yield browser
    if request.node.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)

    browser.quit()

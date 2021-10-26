import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def browser(request):
    # options = Options()
    # options.add_argument("--start-maximized")  # open Browser in maximized mode
    # options.add_argument("--no-sandbox")  # bypass OS security model
    # options.add_argument('--disable-dev-shm-usage')

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "95",
        "screenResolution":"1920x1080x24",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }

    }

    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub", desired_capabilities=capabilities)
    browser.maximize_window()
    # browser = webdriver.Chrome(options=options, executable_path="../chromedriver")
    yield browser
    if request.node.rep_call.failed:
        allure.attach(browser.get_screenshot_as_png(),
                      name=request.function.__name__,
                      attachment_type=allure.attachment_type.PNG)

    browser.quit()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from robot.api.deco import keyword
from locators import BasePageLocators
from robot.api import logger
from selenium.webdriver.chrome.webdriver import WebDriver
TIMEOUT = 4


class BasePage:

    def __init__(self):
        self.driver = None

    @keyword
    def set_driver(self, driver_ex: WebDriver):
        self.driver = driver_ex

    @keyword("go loginator")
    def should_be_login(self):
        logger.info(self.driver.current_url)

    def wait_clickable(self, locator):
        element = WebDriverWait(self.driver, timeout=TIMEOUT).until(EC.element_to_be_clickable(locator))
        return element

    def enter_data(self, locator, data):
        element = self.wait_clickable(locator)
        element.send_keys(data)
        return element

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, timeout=TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"element {locator} not found")
        return element

    @keyword
    def wait_title(self, title):
        # Assert Browser title
        try:
            WebDriverWait(self.driver, timeout=TIMEOUT).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError("Wrong title")

    @keyword
    def should_be_login(self, login, password):
        # Perform login
        self.wait_clickable(BasePageLocators.BUTTON_LOGIN_FORM).click()
        self.enter_data(BasePageLocators.INPUT_LOGIN, login)
        self.enter_data(BasePageLocators.INPUT_PASSWORD, password)
        self.wait_clickable(BasePageLocators.BUTTON_GO_TO_LOGIN).click()

    @keyword
    def should_be_right_username(self, expect_name):
        username = self.wait_visible(BasePageLocators.USERNAME).text
        assert expect_name == username, f"{expect_name} != {username}"
        return username

    def go_to_diff_elements_page(self):
        self.wait_clickable(BasePageLocators.DROPDOWN_HEADER_SERVICE).click()
        self.wait_clickable(BasePageLocators.BUTTON_DIFFERENT_ELEMENTS).click()


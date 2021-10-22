import selenium.webdriver.ie.webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
class BasePage():
    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        self.browser.get(url)

    def wait_title(self, title):
        # Assert Browser title
        try:
            WebDriverWait(self.browser, timeout=4).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError("Wrong title")

    def wait_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=4).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"element with locator {locator} not found")
        return element

    def enter_data(self, locator, data):
        element = self.wait_clickable(locator)
        element.send_keys(data)
        return element

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=4).until(EC.visibility_of_element_located(locator))
        except TimeoutException: raise AssertionError(f"element {locator} not found")
        return element

    def wait_elements(self, locator):
        elements = WebDriverWait(self.browser, timeout=4).until(EC.visibility_of_all_elements_located(locator))
        return elements
    def switch_to_main_frame(self):
        # Switch to original window back
        self.browser.switch_to.default_content()

    def set_dropdawn(self, dropdown_locator, xpath_template, text):
        self.wait_clickable(dropdown_locator).click()
        self.wait_clickable((xpath_template[0], xpath_template[1].format(text))).click()


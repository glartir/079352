from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators
from selenium.webdriver.support.ui import Select
timeout = 4


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        self.browser.get(url)

    def wait_title(self, title):
        # Assert Browser title
        try:
            WebDriverWait(self.browser, timeout=timeout).until(EC.title_is(title))
        except TimeoutException:
            raise AssertionError("Wrong title")

    def wait_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"element with locator {locator} not found")
        return element

    def enter_data(self, locator, data):
        element = self.wait_clickable(locator)
        element.send_keys(data)
        return element

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"element {locator} not found")
        return element

    def wait_elements(self, locator):
        elements = WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def switch_to_main_frame(self):
        # Switch to original window back
        self.browser.switch_to.default_content()

    def set_dropdown_html(self, dropdown_locator, text):
        dropdown = self.wait_clickable(dropdown_locator)
        Select(dropdown).select_by_visible_text(text)
        return dropdown

    def should_be_right_header(self):
        # Assert that there are 4 items on the header section are displayed and they have proper texts
        text_home = self.wait_clickable(BasePageLocators.BUTTON_HEADER_HOME).text
        text_contact = self.wait_clickable(BasePageLocators.BUTTON_HEADER_CONTACT).text
        text_metal = self.wait_clickable(BasePageLocators.BUTTON_HEADER_METALS_COLORS).text
        text_service = self.wait_clickable(BasePageLocators.DROPDOWN_HEADER_SERVICE).text
        return [text_home, text_metal, text_contact, text_service]

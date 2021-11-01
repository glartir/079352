from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.locators import BasePageLocators
from selenium.webdriver.support.ui import Select
import allure

TIMEOUT = 4


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def open_url(self, url):
        with allure.step("Open test site by URL "):
            self.browser.get(url)

    def wait_title(self, title):

        # Assert Browser title
        with allure.step("Assert Browser title "):
            try:
                WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.title_is(title))
            except TimeoutException:
                raise AssertionError("Wrong title")

    def wait_clickable(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise AssertionError(f"element with locator {locator} not found")
        return element

    def enter_data(self, locator, data):
        element = self.wait_clickable(locator)
        element.send_keys(data)
        return element

    def wait_visible(self, locator):
        try:
            element = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f"element {locator} not found")
        return element

    def wait_elements(self, locator):
        elements = WebDriverWait(self.browser, timeout=TIMEOUT).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def switch_to_main_frame(self):
        # Switch to original window back
        with allure.step("Switch to original window back "):
            self.browser.switch_to.default_content()

    def set_dropdown_html(self, dropdown_locator, text):
        dropdown = self.wait_clickable(dropdown_locator)
        Select(dropdown).select_by_visible_text(text)
        return dropdown

    @allure.step("Assert that there are 4 items on the header section are displayed and they have proper texts "):
    def should_be_right_header(self):
        # Assert that there are 4 items on the header section are displayed and they have proper texts

            text_home = self.wait_clickable(BasePageLocators.BUTTON_HEADER_HOME).text
            text_contact = self.wait_clickable(BasePageLocators.BUTTON_HEADER_CONTACT).text
            text_metal = self.wait_clickable(BasePageLocators.BUTTON_HEADER_METALS_COLORS).text
            text_service = self.wait_clickable(BasePageLocators.DROPDOWN_HEADER_SERVICE).text
            return [text_home, text_metal, text_contact, text_service]

    @allure.step("Perform login ")
    def should_be_login(self, login, password):
        # Perform login
        self.wait_clickable(BasePageLocators.BUTTON_LOGIN_FORM).click()
        self.enter_data(BasePageLocators.INPUT_LOGIN, login)
        self.enter_data(BasePageLocators.INPUT_PASSWORD, password)
        self.wait_clickable(BasePageLocators.BUTTON_GO_TO_LOGIN).click()

    @allure.step("Assert Username is loggined ")
    def should_be_right_username(self):
        # Assert Username is loggined
        username = self.wait_visible(BasePageLocators.USERNAME).text
        return username

    @allure.step("Open through the header menu Service -> Different Elements Page ")
    def go_to_diff_elements_page(self):
        self.wait_clickable(BasePageLocators.DROPDOWN_HEADER_SERVICE).click()
        self.wait_clickable(BasePageLocators.BUTTON_DIFFERENT_ELEMENTS).click()

    @allure.step("Assert that there are 5 items in the Left Section are displayed and they have proper text ")
    def should_be_5_items(self):
        # Assert that there are 5 items in the Left Section are displayed and they have proper text
        elements_text = list(map(lambda x: self.wait_visible(x).text, BasePageLocators.LIST_BUTTONS_LEFT_BAR))
        return elements_text

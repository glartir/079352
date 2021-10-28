from pages.base_page import BasePage
from pages.locators import DiffElementsPageLocators
import allure


class DiffElementsPage(BasePage):

    def select_checkboxes(self):
        with allure.step("Select checkboxes "):
            self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER).click()
            self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND).click()

    def select_radio(self):
        with allure.step("Select radio "):
            self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN).click()

    def select_in_dropdown(self, color):
        with allure.step("Select in dropdown "):
            self.set_dropdown_html(DiffElementsPageLocators.DROPDOWN_COLORS, color)

    def check_values(self):

        # Assert that ...
        water = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER)
        wind = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND)
        drop = self.wait_clickable(DiffElementsPageLocators.DROPDOWN_COLORS)
        selen = self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN)
        return water, wind, drop, selen

    def check_log(self):
        log = self.wait_elements(DiffElementsPageLocators.LOG_ENTRIES)
        log_text = [[i.text.split()[1], i.text.split()[-1]] for i in log]
        return log_text






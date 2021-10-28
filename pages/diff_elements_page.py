from pages.base_page import BasePage
from pages.locators import DiffElementsPageLocators
import allure


class DiffElementsPage(BasePage):
    @allure.step("Select checkboxes")
    def select_checkboxes(self):
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER).click()
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND).click()

    @allure.step("Select radio")
    def select_radio(self):
        self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN).click()

    @allure.step("Select in dropdown")
    def select_in_dropdown(self, color):
        self.set_dropdown_html(DiffElementsPageLocators.DROPDOWN_COLORS, color)

    @allure.step("Get dropdown and radio button and checkboxes for assert  their values")
    def check_values(self):
        # Assert that ...
        water = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER)
        wind = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND)
        drop = self.wait_clickable(DiffElementsPageLocators.DROPDOWN_COLORS)
        selen = self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN)
        return water, wind, drop, selen

    @allure.step("Get  rows log row value is for assert corresponded to the selected value")
    def check_log(self):
        log = self.wait_elements(DiffElementsPageLocators.LOG_ENTRIES)
        log_text = [[i.text.split()[1], i.text.split()[-1]] for i in log]
        return log_text






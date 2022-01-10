from BasePage import BasePage
from locators import DiffElementsPageLocators
from robot.api.deco import keyword


class DiffElementsPage(BasePage):

    @keyword
    def select_checkboxes(self):
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER).click()
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND).click()

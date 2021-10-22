from pages.base_page import  BasePage
from pages.locators import DiffElementsPageLocators


class DiffElementsPage(BasePage):

    def select_checkboxes(self):
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER).click()
        self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND).click()

    def select_radio(self):
        self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN).click()

    def select_in_dropdawn(self, color):
        self.set_dropdawn(DiffElementsPageLocators.DROPDOWN_COLORS,
                          DiffElementsPageLocators.DROPDOWN_COLOR_TEMPLATE_VALUE, color)

    # def check_values(self):
    # oops
    #     # Assert that ...
    #     water = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WATER)
    #     wind = self.wait_clickable(DiffElementsPageLocators.CHECKBOX_WIND)
    #     drop = self.wait_clickable(DiffElementsPageLocators.DROPDOWN_COLORS)
    #     selen = self.wait_clickable(DiffElementsPageLocators.RADIOBUTTON_SELEN)
    #
    #     assert water.text == "Water", f"Water != {water.text}"
    #     assert wind.text == "Wind" , f"wind != {wind.text}"
    #     assert selen.text == "Selen", f"Selen != {selen.text}"
    #     # assert drop.text == "Yellow", f"Yellow != {drop.text}"
    #     assert water.find_element_by_xpath("./input").is_selected()
    #     assert wind.find_element_by_xpath("./input").is_selected()
    #     assert selen.find_element_by_xpath("./input").is_selected()
    #

    def check_log(self):
        log = self.wait_elements(DiffElementsPageLocators.LOG_ENTRIES)
        log_text = [[i.text.split()[1], i.text.split()[-1]] for i in log]
        print(log_text)
        assert log_text[0] == ['Colors:', 'Yellow']
        assert log_text[1] == ['metal:', 'Selen']
        assert log_text[2] == ['Wind:', 'true']
        assert log_text[3] == ['Water:', 'true']





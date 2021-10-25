from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):

    def should_be_login(self, login, password):
        # Perform login
        self.wait_clickable(HomePageLocators.BUTTON_LOGIN_FORM).click()
        self.enter_data(HomePageLocators.INPUT_LOGIN, login)
        self.enter_data(HomePageLocators.INPUT_PASSWORD, password)
        self.wait_clickable(HomePageLocators.BUTTON_GO_TO_LOGIN).click()

    def should_be_right_username(self):
        # Assert Username is loggined
        username = self.wait_visible(HomePageLocators.USERNAME).text
        return username

    def should_be_4_images(self):
        # Assert that there are 4 images on the Index Page and they are displayed
        elements = list(map(self.wait_visible, HomePageLocators.LIST_IMAGES))
        return elements

    def should_be_4_text_below(self, ):
        elements_texts = list(map(lambda x: self.wait_visible(x).text.replace("\n", " "),
                                  HomePageLocators.LIST_TEXT_IMAGES))
        return elements_texts

    def should_be_5_items(self):
        # Assert that there are 5 items in the Left Section are displayed and they have proper text
        elements_text = list(map(lambda x: self.wait_visible(x).text, HomePageLocators.LIST_BUTTONS_LEFT_BAR))
        return elements_text

    def should_be_iframe(self):
        # Switch to the iframe and check that there is “Frame Button” in the iframe
        self.browser.switch_to.frame(self.wait_visible(HomePageLocators.FRAME_CARD))
        self.wait_clickable(HomePageLocators.BUTTON_FRAME)

    def go_to_diff_elements_page(self):
        self.wait_clickable(HomePageLocators.DROPDOWN_HEADER_SERVICE).click()
        self.wait_clickable(HomePageLocators.BUTTON_DIFFERENT_ELEMENTS).click()



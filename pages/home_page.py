from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):

    def should_be_4_images(self):
        # Assert that there are 4 images on the Index Page and they are displayed
        elements = list(map(self.wait_visible, HomePageLocators.LIST_IMAGES))
        return elements

    def should_be_4_text_below(self, ):
        elements_texts = list(map(lambda x: self.wait_visible(x).text.replace("\n", " "),
                                  HomePageLocators.LIST_TEXT_IMAGES))
        return elements_texts

    def should_be_iframe(self):
        # Switch to the iframe and check that there is “Frame Button” in the iframe
        self.browser.switch_to.frame(self.wait_visible(HomePageLocators.FRAME_CARD))
        self.wait_clickable(HomePageLocators.BUTTON_FRAME)




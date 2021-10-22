from pages.base_page import BasePage
from pages.locators import HomePageLocators


class HomePage(BasePage):

    def should_be_login(self, login, password):
        # Perform login
        self.wait_clickable(HomePageLocators.BUTTON_LOGIN_FORM).click()
        self.enter_data(HomePageLocators.INPUT_LOGIN, login)
        self.enter_data(HomePageLocators.INPUT_PASSWORD, password)
        self.wait_clickable(HomePageLocators.BUTTON_GO_TO_LOGIN).click()

    def should_be_right_username(self, full_name):
        # Assert Username is loggined
        username = self.wait_visible(HomePageLocators.USERNAME).text
        assert full_name == username, "Usernames not matched"

    def should_be_right_header(self):
        # Assert that there are 4 items on the header section are displayed and they have proper texts
        text_home = self.wait_clickable(HomePageLocators.BUTTON_HEADER_HOME).text
        text_contact = self.wait_clickable(HomePageLocators.BUTTON_HEADER_CONTACT).text
        text_metal = self.wait_clickable(HomePageLocators.BUTTON_HEADER_METALS_COLORS).text
        text_service = self.wait_clickable(HomePageLocators.DROPDOWN_HEADER_SERVICE).text
        assert text_home == "HOME"
        assert text_metal == "METALS & COLORS"
        assert text_contact == "CONTACT FORM"
        assert text_service == "SERVICE"

    def should_be_4_images(self):
        # Assert that there are 4 images on the Index Page and they are displayed
        elements = list(map(self.wait_visible, HomePageLocators.LIST_IMAGES))
        return elements

    def should_be_4_text_below(self, ):
        elements_texts = list(map(lambda x: self.wait_visible(x).text.replace("\n", " "),
                                  HomePageLocators.LIST_TEXT_IMAGES))
        texts = ['To include good practices and ideas from successful EPAM project', 'To be flexible and customizable',
                 'To be multiplatform', 'Already have good base (about 20 internal and some external projects),'
                                        ' wish to get more…']
        assert texts == elements_texts

    def should_be_5_items(self):
        # Assert that there are 5 items in the Left Section are displayed and they have proper text
        elements_text = list(map(lambda x: self.wait_visible(x).text, HomePageLocators.LIST_BUTTONS_LEFT_BAR))
        assert elements_text == ["Home", "Contact form", "Service", "Metals & Colors",
                                 "Elements packs"], f"text button not matched, visible: {elements_text}"

    def should_be_iframe(self):
        # Switch to the iframe and check that there is “Frame Button” in the iframe
        self.browser.switch_to.frame(self.wait_visible(HomePageLocators.FRAME_CARD))
        self.wait_clickable(HomePageLocators.BUTTON_FRAME)




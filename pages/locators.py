from selenium.webdriver.common.by import By


class HomePageLocators:
    BUTTON_HEADER_HOME = (By.CSS_SELECTOR, ".dark-gray .uui-navigation  [href='index.html']")
    BUTTON_HEADER_CONTACT = (By.CSS_SELECTOR, ".dark-gray .uui-navigation  [href='contacts.html']")
    DROPDOWN_HEADER_SERVICE = (By.CSS_SELECTOR, ".dark-gray .uui-navigation .dropdown-toggle")
    BUTTON_HEADER_METALS_COLORS = (By.CSS_SELECTOR, ".dark-gray .uui-navigation  [href='metals-colors.html']")
    BUTTON_LOGIN_FORM = (By.CSS_SELECTOR, ".dark-gray .navbar-right .dropdown-toggle")
    INPUT_LOGIN = (By.CSS_SELECTOR, ".dark-gray #name")
    INPUT_PASSWORD = (By.CSS_SELECTOR, ".dark-gray #password")
    BUTTON_GO_TO_LOGIN = (By.ID, "login-button")
    USERNAME = (By.CSS_SELECTOR, ".dark-gray #user-name")
    LIST_IMAGES = [(By.CSS_SELECTOR, f".benefits .col-sm-3:nth-child({i + 1}) .benefit-icon") for i in range(4)]
    LIST_TEXT_IMAGES = [(By.CSS_SELECTOR, f".benefits .col-sm-3:nth-child({i + 1}) .benefit-txt") for i in range(4)]
    FRAME_CARD = (By.ID, "frame")
    BUTTON_FRAME = (By.ID, "frame-button")
    LIST_BUTTONS_LEFT_BAR = [(By.CSS_SELECTOR, f"#mCSB_1_container #mCSB_1_container  >.left > li:nth-child({i+1})")
                             for i in range(5)]


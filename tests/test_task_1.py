from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.diff_elements_page import DiffElementsPage

def first_4_steps(browser):
    page = HomePage(browser)
    page.open_url('https://jdi-testing.github.io/jdi-light/index.html')
    page.wait_title("Home Page")
    page.should_be_login('Roman', 'Jdi1234')
    page.should_be_right_username("ROMAN IOVLEV")
    return page


def test_exercise1(browser):
    page = first_4_steps(browser)
    page.should_be_right_header()
    page.should_be_4_images()
    page.should_be_4_text_below()
    page.should_be_iframe()
    page.switch_to_main_frame()
    page.should_be_5_items()

def test_exercise2(browser):
    page = first_4_steps(browser)
    page.go_to_diff_elements_page()
    page = DiffElementsPage(browser)
    page.select_checkboxes()
    page.select_radio()
    page.select_in_dropdawn("Yellow")
    page.check_log()



from pages.home_page import HomePage
from pages.diff_elements_page import DiffElementsPage
from delayed_assert import delayed_assert, expect
from tests.users import LOGIN, PASSWORD, USERNAME, URL
import allure


def first_4_steps(browser):
    with allure.step("Open test site by URL "):
        page = HomePage(browser)
        page.open_url(URL)
    with allure.step("Assert Browser title "):
        page.wait_title("Home Page")
    with allure.step("Perform login "):
        page.should_be_login(LOGIN, PASSWORD)
    with allure.step("Assert Username is loggined "):
        expect(page.should_be_right_username() == USERNAME)
    return page


@allure.title("Jdi page suite")
class TestSelenium:
    @allure.title("Check login & iframe")
    @allure.description(""" Check auth, iframe, exist pictures and text below:
    To include good practices and ideas from successful EPAM project',
    'To be flexible and customizable', 'To be multiplatform',
    'Already have good base (about 20 internal and some external projects),'
    ' wish to get more…""")
    @delayed_assert.assert_all()
    def test_exercise1(self, browser):
        page = first_4_steps(browser)
        with allure.step("Assert that there are 4 items on the header section are displayed and they have proper texts "):
            expect(page.should_be_right_header() == ["HOME", "METALS & COLORS", "CONTACT FORM", "SERVICE"], "wrong header")
        with allure.step("Assert that there are 4 images on the Index Page and they are displayed "):
            page.should_be_4_images()
        with allure.step("Assert that there are 4 texts on the Index Page under icons and they have proper text "):
            expect(page.should_be_4_text_below() == ['To include good practices and ideas from successful EPAM project',
                                                     'To be flexible and customizable', 'To be multiplatform',
                                                     'Already have good base (about 20 internal and some external projects),'
                                                     ' wish to get more…'], "wrong text below")
        with allure.step("Assert that there is the iframe with “Frame Button” exist"
                         " & Switch to the iframe and check that there is “Frame Button” in the iframe "):
            page.should_be_iframe()
        with allure.step("Switch to original window back "):
            page.switch_to_main_frame()
        with allure.step("Assert that there are 5 items in the Left Section are displayed and they have proper text "):
            expect(page.should_be_5_items() == ["Home", "Contact form", "Service", "Metals & Colors",
                                                "Elements packs"], "text button not matched")

    @allure.title("Check web-elements")
    @allure.description("Check log on match with values of web-elements")
    @delayed_assert.assert_all()
    def test_exercise2(self, browser):
        page = first_4_steps(browser)
        with allure.step("Open through the header menu Service -> Different Elements Page "):
            page.go_to_diff_elements_page()
            page = DiffElementsPage(browser)
        with allure.step("Select checkboxes "):
            page.select_checkboxes()
        with allure.step("Select radio "):
            page.select_radio()
        with allure.step("Select in dropdown "):
            page.select_in_dropdown("Yellow")
        with allure.step("Assert that dropdown and radio button and checkboxes match their values"):
            water, wind, drop, selen = page.check_values()
            expect(water.text == "Water", f"Water != {water.text}")
            expect(wind.text == "Wind", f"wind != {wind.text}")
            expect(selen.text == "Selen", f"Selen != {selen.text}")
            expect(drop.get_attribute('value') == "Yellow", f"Yellow != {drop.get_attribute('value')}")
            expect(water.find_element_by_xpath("./input").is_selected())
            expect(wind.find_element_by_xpath("./input").is_selected())
            expect(selen.find_element_by_xpath("./input").is_selected())
        with allure.step("Assert that rows log row value is corresponded to the selected value"):
            log = page.check_log()
            expect(log[0] == ['Colors:', 'Yellow'])
            expect(log[1] == ['metal:', 'Selen'])
            expect(log[2] == ['Wind:', 'true'])
            expect(log[3] == ['Water:', 'true'])

    @allure.title("Check make_screenshot when test fail")
    @allure.description("Changed ex2 for fail, check added screenshot")
    @delayed_assert.assert_all()
    def test_exercise2_fail(self, browser):
        page = first_4_steps(browser)
        with allure.step("Open through the header menu Service -> Different Elements Page "):
            page.go_to_diff_elements_page()
            page = DiffElementsPage(browser)
        with allure.step("Select checkboxes "):
            page.select_checkboxes()
        with allure.step("Select radio "):
            page.select_radio()
        with allure.step("Select in dropdown "):
            page.select_in_dropdown("Red")
        with allure.step("Assert that dropdown and radio button and checkboxes match their values"):
            water, wind, drop, selen = page.check_values()
            expect(water.text == "Water", f"Water != {water.text}")
            expect(wind.text == "Wind", f"wind != {wind.text}")
            expect(selen.text == "Selen", f"Selen != {selen.text}")
            expect(drop.get_attribute('value') == "Yellow", f"Yellow != {drop.get_attribute('value')}")
            expect(water.find_element_by_xpath("./input").is_selected())
            expect(wind.find_element_by_xpath("./input").is_selected())
            expect(selen.find_element_by_xpath("./input").is_selected())
        with allure.step("Assert that rows log row value is corresponded to the selected value"):
            log = page.check_log()
            expect(log[0] == ['Colors:', 'Yellow'])
            expect(log[1] == ['metal:', 'Selen'])
            expect(log[2] == ['Wind:', 'true'])
            expect(log[3] == ['Water:', 'true'])

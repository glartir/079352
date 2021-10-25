from pages.home_page import HomePage
from pages.diff_elements_page import DiffElementsPage
from delayed_assert import delayed_assert, expect


def first_4_steps(browser):
    page = HomePage(browser)
    page.open_url('https://jdi-testing.github.io/jdi-light/index.html')
    page.wait_title("Home Page")
    page.should_be_login('Roman', 'Jdi1234')
    expect(page.should_be_right_username() == "ROMAN IOVLEV")
    return page


@delayed_assert.assert_all()
def test_exercise1(browser):
    page = first_4_steps(browser)
    expect(page.should_be_right_header() == ["HOME", "METALS & COLORS", "CONTACT FORM", "SERVICE"], "wrong header")
    page.should_be_4_images()
    expect(page.should_be_4_text_below() == ['To include good practices and ideas from successful EPAM project',
                                             'To be flexible and customizable', 'To be multiplatform',
                                             'Already have good base (about 20 internal and some external projects),'
                                             ' wish to get more…'], "wrong text below")
    page.should_be_iframe()
    page.switch_to_main_frame()
    expect(page.should_be_5_items() == ["Home", "Contact form", "Service", "Metals & Colors",
                                        "Elements packs"], "text button not matched")


@delayed_assert.assert_all()
def test_exercise2(browser):
    page = first_4_steps(browser)
    page.go_to_diff_elements_page()
    page = DiffElementsPage(browser)
    page.select_checkboxes()
    page.select_radio()
    page.select_in_dropdown("Yellow")
    water, wind, drop, selen = page.check_values()
    expect(water.text == "Water", f"Water != {water.text}")
    expect(wind.text == "Wind", f"wind != {wind.text}")
    expect(selen.text == "Selen", f"Selen != {selen.text}")
    expect(drop.get_attribute('value') == "Yellow", f"Yellow != {drop.get_attribute('value')}")
    expect(water.find_element_by_xpath("./input").is_selected())
    expect(wind.find_element_by_xpath("./input").is_selected())
    expect(selen.find_element_by_xpath("./input").is_selected())
    log = page.check_log()
    expect(log[0] == ['Colors:', 'Yellow'])
    expect(log[1] == ['metal:', 'Selen'])
    expect(log[2] == ['Wind:', 'true'])
    expect(log[3] == ['Water:', 'true'])

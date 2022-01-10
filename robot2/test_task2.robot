*** Settings ***

Library  ./BasePage.py  WITH NAME  BasePage
Library  ./DiffElementsPage.py  WITH NAME  DiffElementsPage
Library  ./Selen.py
#Variables  ./locators.py
Test Setup  Start TestCase
Test Teardown  Finish TestCase


*** Keywords ***
Start TestCase
    Open Browser  https://jdi-testing.github.io/jdi-light/index.html  Chrome
    ${driver}  Get Driver
    BasePage.Set Driver  ${driver}
    DiffElementsPage.Set Driver  ${driver}
    Maximize Browser Window

Compare String
    [Arguments]

Finish TestCase
    Run Keyword If Test Failed  Capture Page Screenshot
    Close Browser

*** Test Cases ***

Beuty case2
    BasePage.wait_title  Home Page
    BasePage.should_be_login  Roman  Jdi1234
    BasePage.should_be_right_username  ROMAN IOVLEV
    BasePage.go_to_diff_elements_page
    DiffElementsPage.select_checkboxes
#    Sleep  5s

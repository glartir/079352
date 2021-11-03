*** Settings ***
Library  SeleniumLibrary
Variables  ./locators.py
*** Variables ***

*** Keywords ***
Open Diff Elements Page
    Click Element  ${DROPDOWN_HEADER_SERVICE}
    Click Element  ${BUTTON_DIFFERENT_ELEMENTS}

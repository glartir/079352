*** Settings ***
Library  SeleniumLibrary
Library  String
Library  Collections
Variables  ./locators.py
Resource  ./variables.robot
*** Variables ***

*** Keywords ***

Check and Click
    [Arguments]  ${locator}
    ${element}  Get Webelement  ${locator}
    Element Should Be Visible  ${element}
    Element Should Be Enabled  ${element}
    Click Element  ${element}

Start TestCase
    Open Browser  ${URL}  Chrome
    Maximize Browser Window

Finish TestCase
    Close Browser

Open Diff Elements Page
    Check and Click  ${DROPDOWN_HEADER_SERVICE}
    Check and Click  ${BUTTON_DIFFERENT_ELEMENTS}

Perform login
    [Arguments]  ${name}  ${password}
    Check and Click  ${BUTTON_LOGIN_FORM}
    Input Text  ${INPUT_LOGIN}  ${name}
    Input Password  ${INPUT_PASSWORD}  ${password}
    Check and Click  ${BUTTON_GO_TO_LOGIN}

Assert username
    [Arguments]  ${user_name}
    Element Text Should Be  ${USERNAME_LOCATOR}  ${user_name}

Split and slice
    [Arguments]  ${str}  ${start}  ${finish}=NONE
    @{new_list}  Split String  ${str}
    @{new_list}  Get Slice From List  ${new_list}  ${start}  ${finish}
    [Return]  ${new_list}

Get chain element
    [Arguments]  ${locator1}  ${locator2}
    ${locator_list}  Create List  ${locator1}  ${locator2}
    ${element}  Get Webelement  ${locator_list}
    [Return]  ${element}

Get chain elements
    [Arguments]  ${locator1}  ${locator2}
    ${locator_list}  Create List  ${locator1}  ${locator2}
    @{element}  Get Webelements  ${locator_list}
    [Return]  @{element}

Get Texts From List Elements
    [Arguments]  @{list}
    ${new_list}  Create List
    FOR  ${element}  IN  @{list}
        ${new_element}  Get Text  ${element}
        log  ${new_element}
        Append to list  ${new_list}  ${new_element}
    END
    [Return]  @{new_list}

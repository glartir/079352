*** Settings ***
Library  SeleniumLibrary
Library  String
Library  Collections
Variables  ./locators.py
*** Variables ***
${url}  https://jdi-testing.github.io/jdi-light/index.html
*** Keywords ***
Start TestCase
    Open Browser  ${url}  Chrome
    Maximize Browser Window

Finish TestCase
    Close Browser

Perform login
    [Arguments]  ${name}  ${password}
    Click Element  ${BUTTON_LOGIN_FORM}
    Input Text  ${INPUT_LOGIN}  ${name}
    Input Password  ${INPUT_PASSWORD}  ${password}
    Click Element  ${BUTTON_GO_TO_LOGIN}
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





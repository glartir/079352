*** Settings ***
Library  SeleniumLibrary
Variables  ./locators.py
*** Variables ***

*** Keywords ***
Get Dropdowns elements
    @{dropdowns}  Get WebElements  ${DROPDOWN_USERS}
    [Return]  @{dropdowns}
Get Descriptions elements
    @{descriptions}  Get WebElements  ${DESCRIPTIONS_USERS}
    [Return]  @{descriptions}
Get checkboxes elements
    @{checkboxes}  Get WebElements  ${CHECKBOXES_USERS}
    [Return]  @{checkboxes}
Get usernames elements
    @{usernames}  Get WebElements  ${NICKNAMES_USERS}
    [Return]  @{usernames}
Get numbers elements
    @{numbers}  Get WebElements  ${NUMBER_ID_USERS}
    [Return]  @{numbers}
Check 6 elements
    [Arguments]  ${locator}
    @{items}  Get WebElements  ${locator}
    Element Should Be Visible  ${items}[0]
    Element Should Be Visible  ${items}[1]
    Element Should Be Visible  ${items}[2]
    Element Should Be Visible  ${items}[3]
    Element Should Be Visible  ${items}[4]
    Element Should Be Visible  ${items}[5]

Get texts rows
    [Arguments]  ${id}  ${nickname}  ${description}
    ${id_text}  Get Text  ${id}
    ${nickname_text}  Get Text  ${nickname}
    ${description_text}  Get Text  ${description}
    @{values}  Create List  ${id_text}  ${nickname_text}  ${description_text}
    [Return]  @{values}

Should Be Equal with row
    [Arguments]  ${id}  ${nickname}  ${description}  @{row}
    log  ${row}
    @{text_1}  Get Texts Rows  ${id}  ${nickname}  ${description}
    Should Be Equal As Strings  @{text_1}  @{row}
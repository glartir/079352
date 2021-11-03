*** Settings ***
Library  SeleniumLibrary
Variables  ./locators.py
*** Variables ***

*** Keywords ***
Select chekboxes water and wind
    Click Element  ${CHECKBOX_WATER}
    Click Element  ${CHECKBOX_WIND}
Select radio selen
    Click Element  ${RADIOBUTTON_SELEN}

Select color in dropdwown
    [Arguments]  ${color}
    Select From List By Label  ${DROPDOWN_COLORS}  ${color}
Check values
    ${water}  Get WebElement  ${CHECKBOX_WATER}
    ${wind}  Get WebElement  ${CHECKBOX_WIND}
    ${drop}  Get WebElement  ${DROPDOWN_COLORS}
    ${selen}  Get WebElement  ${RADIOBUTTON_SELEN}
    @{values}  Create List  ${water}  ${wind}  ${drop}  ${selen}
    [Return]  @{values}

##   Checkbox Should Be Selected  ${CHECKBOX_WATER}.Get Webelement  xpath:./input
Check log values
    ${logwindow}  Get Webelements  ${LOG_ENTRIES}
    ${text_color}  Get Text  ${logwindow}[0]
    ${text_metal}  Get Text  ${logwindow}[1]
    ${text_wind}  Get Text  ${logwindow}[2]
    ${text_water}  Get Text  ${logwindow}[3]
    @{values}  Create List  ${text_color}  ${text_metal}  ${text_wind}  ${text_water}
    [Return]  @{values}

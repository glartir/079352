#robot -d robot/results robot/tests/test_task1.robot
*** Settings ***
Library  SeleniumLibrary
Library  String
Library  Collections
Variables  ../Resources/pages/locators.py
Resource  ../Resources/pages/HomePage.robot
Resource  ../Resources/pages/DiffElementsPage.robot
Resource  ../Resources/pages/base.robot
Test Setup  Start TestCase
Test Teardown  Finish TestCase

*** Variables ***
*** Keywords ***
Assert log values
    @{answer}  Check log values
    ${colors}  Split And Slice  ${answer}[0]  1
    @{metal}  Split And Slice  ${answer}[1]  1
    @{wind}  Split And Slice  ${answer}[2]  1
    @{water}  Split And Slice  ${answer}[3]  1

    Should Be Equal As Strings  ${metal}  ['metal:', 'value', 'changed', 'to', 'Selen']
    Should Be Equal As Strings  ${wind}  ['Wind:', 'condition', 'changed', 'to', 'true']
    Should Be Equal As Strings  ${water}  ['Water:', 'condition', 'changed', 'to', 'true']
    Should Be Equal As Strings  ${colors}  ['Colors:', 'value', 'changed', 'to', 'Yellow']
Assert Values
    @{answer}  Check values
    Assert Texts  @{answer}
    Assert Status  @{answer}

Assert Texts
    [Arguments]  @{answer}
    log  ${answer}
    ${water}  Get Text  ${answer}[0]
    ${wind}  Get Text  ${answer}[1]
    ${drop}  Get Value  ${answer}[2]
    ${selen}  Get Text  ${answer}[3]
    Should Be Equal As Strings  ${water}  Water
    Should Be Equal As Strings  ${wind}  Wind
    Should Be Equal As Strings  ${selen}  Selen
    Should Be Equal As Strings  ${drop}  Yellow
Assert status
    [Arguments]  @{answer}
    ${water_status}  Get Chain Element  ${CHECKBOX_WATER}  xpath:./input
    ${wind_status}  Get Chain Element  ${CHECKBOX_WIND}  xpath:./input
    ${selen_status}  Get Chain Element  ${RADIOBUTTON_SELEN}  xpath:./input
    Checkbox Should Be Selected  ${water_status}
    Checkbox Should Be Selected  ${wind_status}
    Checkbox Should Be Selected  ${selen_status}
*** Test Cases ***
Test exercise1
    Title Should Be  Home Page
    Perform login  Roman  Jdi1234
    Assert username  ROMAN IOVLEV
    Open Diff Elements Page
    Select chekboxes water and wind
    Select radio selen
    Select color in dropdwown  Yellow
    Assert Values
    Assert Log Values


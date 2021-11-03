#robot -d robot/results robot/tests/test_gherkin.robot
*** Settings ***
Library  SeleniumLibrary

Variables  ../Resources/pages/locators.py
Resource  ../Resources/pages/HomePage.robot
Resource  ../Resources/pages/UserTablePage.robot
Resource  ../Resources/pages/base.robot

Test Teardown  Finish TestCase
*** Variables ***
${url}  https://jdi-testing.github.io/jdi-light/index.html
@{NUMBERS_TABLE}  1 2 3 4 5 6
@{USERNAMES_TABLE}  Roman  Sergey Ivan  Vladzimir  Helen Bennett  Yoshi Tannamari  Giovanni Rovelli
@{DESCRIPTIONS_TABLE}  Wolverine  Spider Man  Punisher  Captain America some description  Cyclope some description  Hulksome description
*** Keywords ***
I open JDI GitHub site
    Start TestCase
I login as user "Roman Iovlev"
    Perform Login  Roman  Jdi1234
I click on "Service" button in Header
    Click Element  ${DROPDOWN_HEADER_SERVICE}
I click on "User Table" button in Service dropdown
    Click Element  ${BUTTON_USER_TABLE}
"${page}" page should be opened
    Title Should Be  ${page}
6 Number Type Dropdowns should be displayed on Users Table on User Table Page
    Check 6 Elements  ${DROPDOWN_USERS}
6 Usernames should be displayed on Users Table on User Table Page
    Check 6 Elements  ${NICKNAMES_USERS}
6 Description texts under images should be displayed on Users Table on User Table Page
   Check 6 Elements  ${DESCRIPTIONS_USERS}
6 checkboxes should be displayed on Users Table on User Table Page
    Check 6 Elements  ${CHECKBOXES_USERS}
I select 'vip' checkbox for "Sergey Ivan"
    Click Element  ${VIP_SERGEY_IVAN_CHECKBOX}
1 log row has "${target}" text in log section
    ${text_log}  Get Text  ${LOG_ENTRIES}
    @{text_log}  Split And Slice  ${text_log}  1
    @{target}  Split String  ${target}
    Should Be Equal As Strings  ${target}  ${text_log}

User table should contain following values
    [Arguments]  ${numbers_target}  ${name_target}  ${description_targer}
    log   ${numbers_target}[3]
    @{ids}  Get Numbers Elements
    @{nicknames}  Get Usernames Elements
    @{descriptions}  Get Descriptions Elements
#    @{text_1}  Get Texts Rows  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]
#    Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  [1  Roman  Wolverine]
#     Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  ['1', 'Roman', 'Wolverine']
#     Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  ['1', 'Roman', 'Wolverine']
#     Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  ['1', 'Roman', 'Wolverine']
#     Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  ['1', 'Roman', 'Wolverine']
#     Should Be Equal With Row  ${ids}[0]  ${nicknames}[0]  ${descriptions}[0]  ['1', 'Roman', 'Wolverine']

#     log  ${text_1}

*** Test Cases ***
User Table Page test
    Given I open JDI GitHub site
    And I login as user "Roman Iovlev"
    When I click on "Service" button in Header
    And I click on "User Table" button in Service dropdown
    Then "User Table" page should be opened
    And 6 Number Type Dropdowns should be displayed on Users Table on User Table Page
    And 6 Usernames should be displayed on Users Table on User Table Page
    And 6 Description texts under images should be displayed on Users Table on User Table Page
    And 6 checkboxes should be displayed on Users Table on User Table Page
    And User table should contain following values  ${NUMBERS_TABLE}  ${USERNAMES_TABLE}  ${DESCRIPTIONS_TABLE}

#[1,2,3,4,5,6]  [Roman,Sergey Ivan,Vladzimir,Helen Bennett, Yoshi Tannamuri,Giovanni Rovelli]  [Wolverine,Spider Man,Punisher,Captain America some description,Cyclope some description,Hulksome description ]
#        | =Number= | =User= | =Description= |
#        | _1_ | Roman | Wolverine |
#        | _2_ | Sergey Ivan | Spider Man |
#        | _3_ | Vladzimir | Punisher |
#        | _4_ | Helen Bennett | Captain America some description |
#        | _5_ | Yoshi Tannamuri | Cyclope some description |
#        | _6_ | Giovanni Rovelli | Hulksome description |

Exercise3
    Given I open JDI GitHub site
    And I login as user "Roman Iovlev"
    And I click on "Service" button in Header
    And I click on "User Table" button in Service dropdown
    When I select 'vip' checkbox for "Sergey Ivan"
    Then 1 log row has "Vip: condition changed to true" text in log section


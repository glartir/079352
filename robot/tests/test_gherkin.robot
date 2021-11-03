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
@{NUMBERS_TABLE}  1  2  3  4  5  6
@{USERNAMES_TABLE}  Roman  Sergey Ivan  Vladzimir  Helen Bennett  Yoshi Tannamuri  Giovanni Rovelli
@{DESCRIPTIONS_TABLE}  Wolverine  Spider Man  Punisher  Captain America\nsome description  Cyclope\nsome description  Hulk\nsome description
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
    [Arguments]  &{table}
    log   ${table}[number][2]
    @{ids}  Get Numbers Elements
    @{nicknames}  Get Usernames Elements
    @{descriptions}  Get Descriptions Elements
    ${text_ids}  Get Texts From List Elements  @{ids}
    ${text_nicknames}  Get Texts From List Elements  @{nicknames}
    ${text_descriptions}  Get Texts From List Elements  @{descriptions}
    ${table_fact}  Create Dictionary  number  ${text_ids}  user  ${text_nicknames}  description  ${text_descriptions}
    log  ${table_fact}
    Dictionaries Should Be Equal  ${table_fact}  ${table}

droplist should contain values in column Type for user Roman
    [Arguments]  @{droplist}
    @{elements}  Get Web Elements  ${DROPDOWN_VALUES_ROMAN}
    log  ${elements}
    ${droplist_fact}  Get Texts From List Elements  @{elements}
    Lists Should Be Equal  ${droplist}  ${droplist_fact}

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
    And User table should contain following values  number=${NUMBERS_TABLE}  user=${USERNAMES_TABLE}  description=${DESCRIPTIONS_TABLE}

#        | =Number= | =User= | =Description= |
#        | _1_ | Roman | Wolverine |
#        | _2_ | Sergey Ivan | Spider Man |
#        | _3_ | Vladzimir | Punisher |
#        | _4_ | Helen Bennett | Captain America some description |
#        | _5_ | Yoshi Tannamuri | Cyclope some description |
#        | _6_ | Giovanni Rovelli | Hulksome description |
    And droplist should contain values in column Type for user Roman  Admin  User  Manager
         #| Dropdown Values |
         #
         #| Admin           |
         #
         #| User            |
         #
         #| Manager         |

Exercise3
    Given I open JDI GitHub site
    And I login as user "Roman Iovlev"
    And I click on "Service" button in Header
    And I click on "User Table" button in Service dropdown
    When I select 'vip' checkbox for "Sergey Ivan"
    Then 1 log row has "Vip: condition changed to true" text in log section


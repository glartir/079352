*** Settings ***


#Library  SeleniumLibrary
#Library  ./MyLib.py

Library  ./Selen.py
Variables  ./locators.py

*** Test Cases ***

Beuty case
    Open Browser  https://jdi-testing.github.io/jdi-light/index.html  Chrome
    wait clickable  ${CONTACT_FORM}
    Sleep  10s
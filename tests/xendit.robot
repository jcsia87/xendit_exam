*** Settings ***
Library    SeleniumLibrary
Resource    xendit_keywords.robot
Suite Setup    Run Keywords    Open Application
...            AND             Set Selenium Speed  .1
Suite Teardown  Close Browser

*** Variables ***
${URL}    https://www.online-calculator.com/full-screen-calculator/
${BROWSER}    Chrome

*** Test Cases ***
Addition
    [Template]  Add Numbers
    -5  5  0
    5  5  10
    6  6  12

Subtraction
    [Template]  Subtract Numbers
    5  5  0
    6  5  1
    10  5  5

Division
    [Template]  Divide Numbers
    64  4  16
    6  3  2
    # 10  5  5

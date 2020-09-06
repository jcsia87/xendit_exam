*** Settings ***
Library  xendit_keywords.py

*** Keywords ***
Open Application
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Wait Until Element Is Visible  css:#fullframe
    Select Frame  css:#fullframe
    Wait Until Element Is Visible  css:#canvas

Add Numbers
    [Arguments]  ${num1}  ${num2}  ${sum}
    Press Keys  css:#canvas  ${num1}
    Press Keys  css:#canvas  +
    Press Keys  css:#canvas  ${num2}
    Press Keys  css:#canvas  RETURN
    Sum Should Be  ${sum}

Subtract Numbers
    [Arguments]  ${num1}  ${num2}  ${sum}
    Press Keys  css:#canvas  ${num1}
    Press Keys  css:#canvas  -
    Press Keys  css:#canvas  ${num2}
    Press Keys  css:#canvas  RETURN
    Difference Should Be  ${sum}

Divide Numbers
    [Arguments]  ${num1}  ${num2}  ${sum}
    Press Keys  css:#canvas  ${num1}
    Press Keys  css:#canvas  /
    Press Keys  css:#canvas  ${num2}
    Press Keys  css:#canvas  RETURN
    Quotient Should Be  ${sum}

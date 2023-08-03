*** Settings ***

Library    SeleniumLibrary

 

*** Test Cases ***

Login exitoso

    Entrar al sitio

    Entrar al inicio de sesion

    Ingresar credenciales

 

 

*** Keywords ***

Entrar al sitio

    Open Browser    https://magento.softwaretestingboard.com/     gc

    Maximize Browser Window

   

Entrar al inicio de sesion

    Click Element    //div[@class="panel header"]//a[contains(text(), "Sign In")]

    Wait Until Element Is Visible    //span[@data-ui-id="page-title-wrapper"]    20s

   

Ingresar credenciales

    Input Text    //input[@id="email"]    test.123@automation.com

    Input Text    //fieldset//input[@id= "pass"]    Test.123

    Click Element    //*[@id="send2"]/span
*** Settings ***
Library    SeleniumLibrary
Resource    Data_source.robot
Resource    Locators.robot

*** Keywords ***
Entrar al sitio
    Open Browser    ${URL}     gc
    Maximize Browser Window
    
Entrar al inicio de sesion
    Click Element    ${HOME_SIGNIN_BTN}
    Wait Until Element Is Visible    //span[@data-ui-id="page-title-wrapper"]    ${TIMEOUT}
    
Ingresar credenciales
    Input Text    //input[@id="email"]    ${USER}
    Input Text    //fieldset//input[@id= "pass"]    ${PASS}
    Click Element    //*[@id="send2"]/span
    Wait Until Element Is Visible    //span[text() = "Shop New Yoga"]    ${TIMEOUT}
    
Buscar un elemento
    Input Text    //input[@id = "search"]    ${ITEM_NAME}
    Press Keys    None    ENTER
    Wait Until Element Is Visible    //span [ text() = "Search results for: '${ITEM_NAME}'"]

Seleccionar un elemento
    Click Element    //img[@alt="Josie Yoga Jacket"]
    Wait Until Element Is Visible    //span[text()="Josie Yoga Jacket"]    ${TIMEOUT}
    
    # SIZE CONDITION
    ${STATUS}    Run Keyword And Return Status    Wait Until Element Is Visible    //span[@id="option-label-size-143"]    ${TIMEOUT}    # Esto es el Size
    IF    ${STATUS}==${True}
        Click Element    //div[contains (@id, "size")][1]

    END    
    # COLOR CONDITION
    ${STATUS}    Run Keyword And Return Status    Wait Until Element Is Visible    //span[@id="option-label-color-93"]    ${TIMEOUT}    # Esto es el Size
    IF    ${STATUS}==${True}
        Click Element    //div[contains (@id, "color")][1]
        
    END  
    ${random}=    Evaluate    random.randint(1, 5)
    Input Text    //input[@name="qty"]    ${random}
    Click Element    //button[@title="Add to Cart"]
    Click Element    //a[contains(@class,"showcart")]
    Wait Until Element Is Visible    //a[contains(text(),"Josie Yoga Jacket")]    ${TIMEOUT}

Teardown tc
    [Arguments]    ${COMOSEA}
    Set Test Message    ${COMOSEA}
    Close All Browsers
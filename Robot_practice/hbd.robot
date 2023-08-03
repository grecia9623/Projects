*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${BROWSER}    Chrome
${URL}    https://www.facebook.com
${USERNAME}    tu_usuario_de_facebook
${PASSWORD}    tu_contraseña_de_facebook
${FRIEND_NAME}    Nombre del amigo
${BIRTHDAY_MESSAGE}    Feliz cumpleaños, que tengas un día maravilloso lleno de alegría. Te quiero.

*** Test Cases ***
Enviar Felicitacion de Cumpleaños en Facebook
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Log In to Facebook
    Find Friend's Birthday
    Send Birthday Greeting
    Close Browser

*** Keywords ***
Log In to Facebook
    Input Text    name=email    ${USERNAME}
    Input Password    name=pass    ${PASSWORD}
    Click Button    //input[@value='Iniciar sesión']

Find Friend's Birthday
    # Cambia "Friend's Name" por el nombre de tu amigo de cumpleaños
    Input Text    name=q    ${FRIEND_NAME}
    Click Element    //button[@data-testid='facebar_search_button']
    Click Link    //span[text()='${FRIEND_NAME}']
    Wait Until Element Is Visible    //span[text()='Cumpleaños']
    Click Link    //span[text()='Cumpleaños']

Send Birthday Greeting
    Input Text    name=message    ${BIRTHDAY_MESSAGE}
    Click Button    //button[@data-testid='photo_upload_composer']
    Sleep    2s
    Click Link    //span[text()='Publicar']

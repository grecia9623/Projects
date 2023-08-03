*** Settings ***
Resource    Keywords_repository.robot

*** Test Cases ***
Login exitoso
    [Documentation]    TC Description
    Entrar al sitio
    Entrar al inicio de sesion
    Ingresar credenciales
    Teardown tc    Se inició sesión correctamente

Comprar un articulo
    Entrar al sitio
    Entrar al inicio de sesion
    Ingresar credenciales
    Buscar un elemento
    Seleccionar un elemento
    Teardown tc    Se agregó el item correctamente

#Actividad funciones Edutin Academy
import sys
print("Conversor de monedas")
moneda_actual = int(input("Ingrese la moneda que quiere convertir 1.Dolar 2.Euro : "))
moneda_a_convertir = input("¿A que moneda deseas convertir? \n1 Pesos colombianos \n2 Yunes \n3 Libras Esterlinas \n4 Pesos mexicanos \n")
valor = float(input("Ingrese la cantidad a convertir: \n"))
def conversor(moneda_actual,valor,moneda_a_convertir):
    if moneda_actual == 1:
        def dolarTo(): #subfuncion
            if moneda_a_convertir == "1":
                print(f'${valor} dolares equivalen a {valor * 3750} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'${valor} dolares equivalen a {valor * 6.37} yuanes')
            elif moneda_a_convertir == "3":
                print(f'${valor} dolares equivalen a {valor * 0.76} libras esterlinas')
            elif moneda_a_convertir == "4":
                print(f'${valor} dolares equivalen a {valor * 17.99} pesos mexicanos')
            else:
                print("Error, seleccione una opcion valida")
        dolarTo()
    elif moneda_actual == 2:
        def euroTo(): #subfuncion
            if moneda_a_convertir == "1":
                print(f'€{valor} euros equivalen a {valor * 4000} pesos colombianos')
            elif moneda_a_convertir == "2":
                print(f'€{valor} euros equivalen a {valor * 6.93} yuanes')
            elif moneda_a_convertir == "3":
                print(f'€{valor} euros equivalen a {valor * 0.83} libras esterlinas')
            elif moneda_a_convertir == "4":
                print(f'€{valor} euros equivalen a {valor * 19.88} pesos mexicanos')
            else:
                print("Error, seleccione una moneda a convertir valida")
        euroTo()
    else:
        print("Error, seleccione 1.Dolar o 2.Euro")
conversor(moneda_actual,valor,moneda_a_convertir)
"""
50 dolares a pesos colombianos = 187500.0
30 euros a yuanes = 207.89999999999998 yuanes
15 euros a libras esterlinas = 12.45 libras esterlinas
"""
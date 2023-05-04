#funciones con parametros

def multiplicacion(numero = None):
    if numero == None:
        print(input("Introduce un numero"))
    else:
        print(f"Tabla de multiplicar del numero {numero}: ")
        for i in range(1,21):
            print(f'{numero} X {i} = {numero * i}')


multiplicacion(5)
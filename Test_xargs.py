def suma(a, b):
    print(a + b)


suma(2, 5)
def suma_varios_numeros(*numeros):#El *convierte Parametros en #iterable
    resultado = 0
    for numero in numeros: #for para recorrer el iterable
        resultado += numero
# A la variable que tengo a la izquierda sumale el numero del iterable 
# y asigna el resultado a la misma variable (ya sea + , - , * o / )
    print(resultado)

suma_varios_numeros(8, 4, 9, 1 ,2)

def resta(*numeros): #iterable
    resultado = 0
    for numero in numeros: #for para recorrer el iterable
        resultado -= numero
# A la variable que tengo a la izquierda restale el numero del iterable 
# y asigna el resultado a la misma variable (ya sea + , - , * o / )
    print(resultado)

resta(9, 1 ,2)
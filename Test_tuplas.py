#Tuplas

"""
Guardan los datos separados por comas, son inmutables, no permiten cambiar los datos almacenados
requieren poco espacio en memosrio
count = saber cuantas veces existe un dato
index = saber cual es la posicion

Crear una tupla con numeros, solicitar que se ingrese un numero y mostrar cuantas veces existe en la tupla
"""

numeros = (3,4,2,6,4,9,1,12,3,34,2,56,23,12,11,15,97)

n = int(input("Ingresa un numero: "))
#print("El numero se repite " + str(numeros.count(n)) + " veces.")
print("El numero " + str(n) + " se encuentra en el indice " + str(numeros.index(n)))
#en index arroja la posicion que encuentre primero en la tupla
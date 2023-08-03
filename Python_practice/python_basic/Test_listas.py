#LISTAS
numeros = [1, 2, 3]
print(numeros)

#feo
primero = numeros[0]
primero = numeros[1]
primero = numeros[2]

#DESEMPAQUETAR LISTAS
pri ,seg, ter = numeros
print(pri, seg, ter)

#DESEMPAQUETAR UN ELEMENTO DE LISTAS 
pri, *otros = numeros
print(pri)

pri, seg, *otros = numeros
print(seg)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pri, *otros, ultimo = numeros
print(pri, ultimo)

#LISTAS STRINGS
super = ["Pan", "cafe", "azucar"]
print(super)

#LISTAS BOOLEAN
booleans = [True, False, True, True]
#LISTAS MATRIZ
matriz = [[0,1], [1,2]]
#LISTAS un numero muchas veces
ceros = [0] * 10
print(ceros)
#LISTAS varios numeros muchas veces
cero_dos = [0,2] * 10
print(cero_dos)
#COMBINAR LISTAS
alfanumerico = numeros + super
print(alfanumerico)
#LISTAS CON RANGO DEL 1 al 11
rango = list(range(1,11))
print(rango)
#LISTAS de un STRING
chars = list("hola mundo")
print(chars)

#MANIPULAR LISTAS Y ACCEDER A LOS DATOS DE UNA LISTA
mascotas = ["Pelusa", "Nala", "Luna", "Copito"]
print(mascotas)
print(mascotas[2:])
print(mascotas[-1])# cero es pelusa -1 no hay nada entonces se va al final Copito

print(mascotas[::2])#Solo toma los pares 
#Toma el primero[0], el siguiente saltalo[1], toma el siguiente[2] ,el sig saltalo [3]...
print(mascotas[1::2]) #Comienza tomando[1], el siguiente saltalo[2],toma el siguiente[3] ...

print(mascotas[1:2:2]) #Comienza tomando[1], el siguiente saltalo[2],Se indico termina hasta que llegue a [2]

numeros = list(range(1,21)) #Da impares
print(numeros[::2])

numeros = list(range(21)) 
print(numeros[::2]) #Da pares
print(numeros[1::2]) #Da impares

numeros = list(range(1,21)) #Da pares 
print(numeros[1::2])
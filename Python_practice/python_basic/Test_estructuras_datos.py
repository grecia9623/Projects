#Estructuras de datos

#Listas : la lista es la estructura mas sencilla
#lista = [0,1,2,3,4,5] la posicion en una lista inicia en 0
#sus elementos pueden modificarse
#para acceder se utiliza el indice

"""list = [0,1,2]
print(list[0])

#escribir un programa que almacene las asignaturas de un curso
asignaturas= ["Matematicas","Español","Ingles","Historia"]
print(type(asignaturas))
print(asignaturas[0])

#Loteria
numeros = []
for i in range(6):
    numeros.append(int(input("Introduce un numero :"))) #append es un metodo de lista

numeros.sort()
print(f'Los numero ganadores son: {numeros}') #metodo de lista para organizar de menor a mayor
"""
lista = [23,"grecia","23/sep/1996",6,6,6]
for i in lista:
    print(i)

#lista.remove(23) #metodo para eliminar un elemento de una lista
#for i in lista:
#    print(i)

#lista.pop(0) #metodo para eliminar por posicion
#for i in lista:
#    print(i)

#metodo para eliminar posicion en la lista se usa con corchetes
#del lista[1]
#for i in lista:
#    print(i)

#Metodo para vaciar la lista
#lista.clear()
#print("metodo clear" + str(lista))

#metodo para encontrar cuantos elementos hay del valor ingresado en el metodo
print(lista.count(6))

#metodo para saber la posicion de un valor en la lista
print(lista.index("grecia"))

#Metodo para intercambiar la posicion de los elementos
lista.reverse()
print(lista)

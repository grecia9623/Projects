#Conjuntos
#no se repiten y no estan en forma ordenada
"""
add Añade un elemento al final del conjunto
clear Elimina toda la info del conjunto
pop Devuelve y elimina un elemento arbitrario o devuelve error si esta vacio
remove Intenta eliminar un elemento del conjunto, si no existe devuelve error
union Devuelve un conjunto con todos los elementos de ambos conjuntos
"""
#primera forma de crear conjuntos
alumnos = {"Andrea", "Ruby", "Marcos","Marlon","Jose","Jose"} #Si le agrego dos iguales solo se devuelve uno
print(type(alumnos)) #devuelve tipo SET que es un conjunto
print(alumnos)

#segunda forma de crear conjuntos
lenguajes = set({"PHP","Python","Java","C"})
#print(lenguajes)

lenguajes.add("Javascript") #añadimos un elemento al conjunto
#print(lenguajes)

#lenguajes.clear()
#print(lenguajes) #devuelve vacio

#lenguajes.pop()
#devuelve error si esta vacio el conjunto , si no esta vacio elimina un elemento del conjunto de manera arbitraria
#print(lenguajes)

lenguajes.remove("Java") #Intenta eliminar un elemento que se ingrese en el parentesis, si no existe arroja error
#si existe el elemento lo elimina
#print(lenguajes)

todos = alumnos.union(lenguajes) #unir dos conjuntos
print(todos)
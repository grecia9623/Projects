

"""
mascotas = ["Pelusa", "Nala", "Luna", "Copito"] #Lista iterable
print(mascotas.index("Nala"))
"""

mascotas = ["Pelusa", "Nala", "Luna", "Copito", "Nala"] #Lista iterable
if "Nala" in mascotas:
    print(mascotas.index("Nala"))  # SI EXISTE MAS DE UN MISMO ELEMENTO, SOLO NOS INDICA EL INDICE DEL PRIMERO QUE ENCUENTRA
else:
    print("No se encontro")
#BUSCA CUANTAS VECES EXISTE UN ELEMENTO EN LA LISTA
print(mascotas.count("Nala"))

#AGREGAR Y ELIMINAR ELEMENTOS

#AGREGAR
mascotas.insert(1, "Pelusa")
mascotas.append("Firulais") #SE AGREGA AL FINAL
print(mascotas)
#ELIMINAR
mascotas.remove("Nala") #SOLO BORRA EL PRIMER NALA QUE ENCUENTRA
mascotas.pop() # ELIMINA EL ULTIMO REGISTRO
mascotas.pop(1) #ELIMINA EL REGISTRO DEL INDICE 1
del mascotas[2] #Elimina el registro del indice 2
mascotas.clear() #ELIMINA TODOS LOS REGISTROS DE LA LISTA []
print(mascotas)

#ORDENAR ELEMENTOS DE UNA LISTA
numeros = [5656, 3434, 23445, 5465, 2, 232323, 34]
numeros.sort() #ordena elementos del menor al mayor
print(numeros)
numeros.sort(reverse=True) #ordena elementos del mayor al menor
print(numeros)
#ORDEN DE ELEMENTOS MENOR AL MAYOR EN UNA NUEVA LISTA
numeros2 = sorted(numeros)
print(numeros2)

#ORDEN DE ELEMENTOS MAYOR AL MENOR EN UNA NUEVA LISTA
numeros2 = sorted(numeros, reverse=True)
print(numeros2)

#CON PALABRAS
usuarios = [
    ["Brenda",3],
    ["Danna", 1],
    ["Adriana", 2]
]
#usuarios.sort() #ORDENA LO QUE ENCUENTRA EN EL PRIMER INDEX A-Z o 1-n
"""
def ordena(elemento):
    return(elemento[1]) # RETORNA POR EL INDEX 1 (QUE ES EL ID)
usuarios.sort(key=ordena)
print(usuarios)
"""
#OREDENA POR EL ID (index 1)
def ordena(elemento):
    return(elemento[1]) # RETORNA POR EL INDEX 1 (QUE ES EL ID)
usuarios.sort(key=ordena, reverse=True)
print(usuarios)


#LAMBDA
usuarios.sort(key=lambda el:el[1], reverse=True)
print(usuarios)


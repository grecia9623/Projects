#Diccionarios

#Elementos cada uno tiene una llave y un valor, cuenta con metodos para insertar, limpiar, eliminar, devolver llaves
#y devolver valores en forma de listas

diccionario = {
    "Key": "Sara",
    "Edad": 28,
    "Documentos": 456234
}
print(diccionario)

#Segunda forma de crear diccionario
diccionario_forma_dos = dict(Nombre='Paola',
                             Edad=37,
                             Documento=2394534)
print(diccionario_forma_dos)

#Tercera forma de crear diccionario
diccionario_forma_tres = dict([
    ('Nombre','Jose'),
    ('Edad',54),
    ('Documento',657474)
])
print(diccionario_forma_tres)

#Ejemplo
inventario = {"Manzanas":235,"Peras":6,"Naranjas":45,"Sandias":52}
#print(inventario.keys())  #Devuelve las llaves del diccionario
print(inventario.values()) #devuelve los valores del diccionario
print(inventario.items()) #devuelve los elementos en forma de lista
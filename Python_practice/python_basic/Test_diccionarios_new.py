
#La llave solo acepta strings y el valor puede ser cualquier cosa
punto = { "x": 25,
          "y": 50}
#print(punto)

#podemos acceder mediante el string
#print(punto["x"])
#print(punto["y"])

#AGREGAR NUEVA LLAVe
"""
punto["z"] = 45
print(punto)
if "x" in punto:
    print("encontre x", punto["x"]) #mensaje y valor de la llave
"""
    
diccionario = {
    "Key": "001",
    "Edad": 28,
    "Documentos": 456234
}
print(diccionario)

#metodo get
print(diccionario.get("Key"))
#print(diccionario.get("Nombre")) si no existe devuelve None
print(diccionario.get("Nombre", "Sara"))
del diccionario["Documentos"]
del(diccionario["Key"])

diccionario["Nombre"] = "Sara"
print(diccionario)

for valor in diccionario:
    print(valor, diccionario[valor])

for valor in diccionario.items():
    print(valor) #DEVUELVE TUPLAS

for llave, valor in diccionario.items():
    print(llave, valor) 

usuarios = [
    {"id": "000001",
     "usuario": "grecia12",
     "nombre": "Grecia Lopez",
     "correo": "grecia judith lopez suazo",
     "telefono": 3333112233},
    {"id": "000002",
     "usuario": "daniela23",
     "nombre": "Daniela Perez",
     "correo": "dadiela@gmail.com",
     "telefono": 3399118833},
    {"id": "000002",
     "usuario": "juandom",
     "nombre": "Juan Dominguez",
     "correo": "juan@gmail.com",
     "telefono": 3388338833},
]
for usuario in usuarios:
    print(usuario["nombre"])
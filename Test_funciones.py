def hola(nombre,apellido):#parametro
    print(f"Hola {nombre} {apellido}")

hola("Grecia", "Lopez")#argumento

#parametros opcionales
def hola(nombre,apellido="Feliz"):#parametro
    print(f"Hola {nombre} {apellido}")

hola("Grecia")#argumento

#Argumentos nombrados, pueden no estar en orden pero con el nombre lo podemos utilizar,
#tienen que estar nombrados todos los argumentos
hola(apellido="Lopez", nombre="Grecia")


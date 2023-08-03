
nombre = '    Juan RIOS montes          n'

print(nombre.upper())
print(nombre.lower())
print(nombre.strip().capitalize())
print(nombre.title())
print(nombre.lstrip())  #lstrip es left para eliminar los espacios de la izquierda
print(nombre.lstrip())  #rstrip es right para eliminar los espacios de la derecha
print(nombre.find("u")) #Devuelve el indice y si no la encuentra va a devolver -1
print(nombre.replace("u", "o"))
print("IOS" in nombre) #Devuelve el boolean TRUE SI encuentra la cadena de caracteres y si NO se encuentra devuelve FALSE
print("Vega" not in nombre) #Devuelve el boolean TRUE si NO se encuentra la cadena de caracteres y SI la encuentra devuelve FALSE

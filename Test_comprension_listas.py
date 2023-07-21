#LISTAS DE COMPRENSION
usuarios = [
    ["Brenda",3],
    ["Danna", 1],
    ["Adriana", 2]
]
"""
#DE USUARIOS A NOMBRES
nombres = []
for usuario in usuarios:
    nombres.append(usuarios[0])
print(nombres)
"""
#nombres = [expresion(for item in items)] #ESTRUCTURA

"""
nombres = [usuario[0] for usuario in usuarios] #TOMAMOS LA LISTA USUARIOS Y APLICAMOS UNA TRANSFORMACION AL ELEMENTO [0] 
print(nombres)
"""

"""
#FILTRAR LISTA
nombres = [usuario for usuario in usuarios if usuario[1] < 2] #TOMAMOS LA LISTA USUARIOS Y APLICAMOS UNA TRANSFORMACION AL ELEMENTO [0] 
print(nombres)
"""

#MODIFICAR Y FILTRAR
"""
nombres = [usuario[0] for usuario in usuarios if usuario[1] < 2] #TOMAMOS LA LISTA USUARIOS Y FILTRAMOS 
print(nombres)
"""

#TOMAMOS LA LISTA USUARIOS Y APLICAMOS UNA TRANSFORMACION AL ELEMENTO [0]
#nombres = list(map(lambda usuario: usuario[0], usuarios))
#print(nombres)

#TOMAMOS LA LISTA USUARIOS Y FILTRAMOS 
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios)) # AL FINAL LE ESTAMOS INDICANDO LA LISTA
print(menosUsuarios)

"""
mascotas = ["Pelusa", "Nala", "Luna", "Copito"] #Lista iterable

for mascotas in mascotas:
    print(mascotas)
"""
    
mascotas = ["Pelusa", "Nala", "Luna", "Copito"] #Lista iterable
for mascotas in enumerate(mascotas): #Devuelve tupla
    print(mascotas) #print(mascotas[0])  print(mascotas[1])


mascotas = ["Pelusa", "Nala", "Luna", "Copito"] #Lista iterable 
for indice, mascota in enumerate(mascotas): #ACCEDER A LOS INDICES DE LA LISTA
    print(indice, mascota)
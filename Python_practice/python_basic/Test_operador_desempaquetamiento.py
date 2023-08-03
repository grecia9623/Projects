#Listas
lista1 = [1,2,3]

lista2 = [4,5,6]

combinada = [*lista1, *lista2]

#serviria para una funcion que tengamos que pasarle varios parametros pero estos se encuentren en una lista
#datos(num1,num2,num3)

combinada = ["Hola", *lista1, "mundo", *lista2, "Grecia"]
print(combinada)



#Diccionarios
punto1 = { "x": 25, "x": 12} # reempolaza el 25 por el 12

punto2 = { "y": 50}

combinada2 = {**punto1, **punto2}
print(combinada2)

combinada3 = {**punto1, "lala": "hola", **punto2, "z": 5}
print(combinada3)



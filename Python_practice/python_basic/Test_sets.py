#SET significa grupo o conjunto, ELIMINA LOS DUPLICADOS
primer = {1,2,3,3,4,5}
primer.add(6)
primer.remove(1)
print(primer)

#Crear un set desde una lista
segundo = [5,6,7,8,9]
segundo = set(segundo)
print(segundo)

#Crear un set desde una tupla
tercero = (9,10,11,12)
tercero = set(tercero)
print(tercero)

#Union de SET |
print(primer | segundo | tercero)

#INTERSECCION &
print(primer & segundo)

#DIFERENCIA - ELIMINA los que son iguales (9 y 9 SE BORRARAN)
print(segundo - tercero)

# ^ DIFERENCIA SIMETRICA 1 2 3   2 3 4 borra 23 
numerito = {1,2,3}
numerote = {2,3,4}
print(numerito ^ numerote)

if 1 in numerito:
    print("Se encontro")
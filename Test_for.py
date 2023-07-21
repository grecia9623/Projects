

#not lo convierte a el contrario de True o False 

#for

for numero in range(5):
    print(numero)

print(3 * "Grecia")


#----------------------------------------FOR ELSE
buscar = 25
for x in range(4): #range(4) es un iterabe (como tuplas, strings, listas etc.)
    if x == buscar:
        print("encontrado, adios", x)
        break
else:
    print("No encontre el numero")
#-----------------------------------------
# for para un string iterable
for caracter in "Ultimate python":
    print(caracter)
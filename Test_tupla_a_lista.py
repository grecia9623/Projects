#Una tupla es lo mismo que la lista pero la tupla no es modificable
# Definición de una tupla 'numeros' que se crea concatenando dos tuplas.
# Las tuplas son inmutables, es decir, no se pueden modificar después de ser creadas.
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)  # Imprime: (1, 2, 3, 4, 5, 6)

# 'punto' es inicialmente una lista mutable.
punto = [1, 2]

# Usando la función 'tuple' para convertir una lista en una tupla.
punto = tuple([1, 2])
punto = tuple(["Grecia", "Judith"])  # Ahora 'punto' es una tupla inmutable.
print(punto)  # Imprime: ("Grecia", "Judith")

# Creación de una nueva tupla 'menosNumeros' que contiene los tres primeros elementos de 'numeros'.
menosNumeros = numeros[:3]  # Nueva tupla: (1, 2, 3)
print(menosNumeros)

# Asignación múltiple de valores de la tupla 'numeros' a variables individuales.
# El operador '*' permite agrupar los elementos restantes en una lista 'otros'.
primero, segundo, *otros = numeros
print(primero, segundo, otros)  # Imprime: 1 2 [3, 4, 5, 6]
print(segundo)  # Imprime: 2
print(otros)    # Imprime: [3, 4, 5, 6]

# Iteración a través de la tupla 'numeros' e impresión de cada elemento.
for n in numeros:
    print(n)

# Conversión de la tupla 'numeros' en una lista 'listaNumeros'.
listaNumeros = list(numeros)  # Ahora 'listaNumeros' es una lista mutable.

listaNumeros[0] = "Mod"
print(listaNumeros)
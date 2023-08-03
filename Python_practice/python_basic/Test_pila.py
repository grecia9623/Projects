#FIFO

#historial de navegacion p.e. regresar la pagina

#ES IGUAL A LA IMPLEMENTACION DE UNA LISTA PERO PARA QUE FUNCIONE CORRECTAMENTE SE USA APPEND Y POP

pila = []
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

ultimoElemento = pila.pop()  #ELIMINAR EL ULTIMO ELEMENTO

print(ultimoElemento)
print(pila)

print(pila[-1]) #saber el ultimo elemento
pila.pop()
pila.pop()
if not pila:
    print("Pila vacia")
def suma(a,b):
    resultado = a + b
    print(resultado)

suma(1, 2)
#return
def suma_return(e, f):
    resultado = e + f
    return resultado

g = suma_return(1, 2)
h = suma_return(g, 1000)
print(h)
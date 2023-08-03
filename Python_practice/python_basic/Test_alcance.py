saludo = "Hola Global" # no se recomienda Usar variables globales
'''
contexto global
'''
def saludar():
    saludo = "hola"
    print(saludo)

def saludaGrecia():
    saludo = "Buenas tardes"
    print(saludo)

saludar()
print(saludo)
saludaGrecia()
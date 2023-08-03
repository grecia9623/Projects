
saludo = "Hola Mundo"
print(type(saludo))

#clase es el plano de construccion
#objeto: es una instancia de una clase

"""
Pascal Case, Upper Camel Case 
SE DEBE PONER MAYUSCULA EN LA PRIMERA LETRA 
DE LA CLASE Y SIN ESPACIOS p.e. PerrosDeChina
Para poder diferenciar cuando se esta creando instancia de una clase p.e. Perro()
De invocar una funcion generar_reporte()
"""

class Perro: 
    #CONSTRUCTOR
    #Self es una referencia a la instancia de la clase
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice Guau tengo {self.edad} años")

mi_perro = Perro("Luna", 2)
mi_perro.patas = 2 #Solo cambia el valor en la instancia
mi_perro2 = Perro("Nala", 8)

mi_perro.habla()
mi_perro2.habla()

print(Perro.patas)
print(mi_perro.patas)
"""
Cuando una funcion esta dentro de la clase
la funcion se convierte en METODO


mi_perro = Perro()
print(type(mi_perro)) 
#__main__ es el modulo donde se crea la clase

mi_perro.habla() #metodos que podemos crear

print(isinstance(mi_perro, Perro)) 
#Si la instancia esta dentro de la clase devuelve True
"""

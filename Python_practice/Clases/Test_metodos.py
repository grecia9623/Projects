class Perro: 
    #CONSTRUCTOR
    #Self es una referencia a la instancia de la clase
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau")

    @classmethod
    def factory(cls):
        return cls("Milo", 9)   

Perro.habla()
perro1 = Perro("Luna", 4)
perro2 = Perro("Camila", 11)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)

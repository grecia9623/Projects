#PROPIEDADES Y METODOS PRIVADOS

class Perro: 
    #CONSTRUCTOR

    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    def get_nombre(self):
        return self.__nombre
    
    def habla(self):
        print(f"{self.__nombre} Guau")

    @classmethod
    def factory(cls):
        return cls("Milo", 9)  
    
perro1 = Perro.factory()
perro1.habla()
print(perro1.get_nombre())
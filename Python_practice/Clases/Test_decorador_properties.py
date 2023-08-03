class Perro:
    def __init__(self, nombre):
        self.nombre = nombre
    
    @property
    def nombre(self): #GET
        print("Paso getter")
        return self.__nombre
    
    @nombre.setter #SET
    def nombre(self, nombre):
        print("Paso setter")
        if nombre.strip():
            self.__nombre = nombre

perro = Perro("Carlos")
print(perro.nombre)
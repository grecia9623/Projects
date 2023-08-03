from abc import ABC, abstractmethod

class Model(ABC): #No se puede instanciar una clase abstracta
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD") #indica que se esta guardando la tabla en la base de datos

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("guardando usuario")

user = Usuario()
user.guardar()
Usuario.buscar_por_id(123)
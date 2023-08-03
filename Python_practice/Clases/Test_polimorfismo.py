from abc import ABC, abstractmethod

class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass

class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")

def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()

#instancia de usuario
user = Usuario()
#guardar(user)

#instancia de sesion
sesion = Sesion()
guardar([sesion, user]) # le entregamos a la funcion dos objetos (POLIMORFISMO)
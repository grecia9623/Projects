class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion():
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
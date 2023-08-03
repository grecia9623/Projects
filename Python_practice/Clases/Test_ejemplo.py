class Model():
    tabla = False
    def __init__(self):
        if not self.tabla: #Verificar si se definio una tabla en la clase hijo
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD") #indica que se esta guardando la tabla en la base de datos

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por ID {_id} en la tabla {self.tabla}")

class Usuario(Model):
    tabla = "Usuario"

user = Usuario()
user.guardar()
user.buscar_por_id(123)
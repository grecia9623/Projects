#Clases objetos y metodos en python

#Las clases son plantillas que contienen metodos y atributos
#y sirven para crear objetos
#Los objetos son una instancia de la clase
class Bicicleta:
    def __init__(self,color,cambios,rin):
        self.color = color
        self.cambios = cambios
        self.rin = rin

    def frenar(self):
        return "La bici esta frenando"

    def avanzar(self):
        return "La bici esta avanzando"

    def girar(self):
        return "La bici esta girando"

urbana = Bicicleta("Rojo",8,27.5)
hibrida = Bicicleta("Azul",1,29)

print("Urbana:" + str(urbana.color))
print("Comportamiento de la bicicleta urbana: " + str(urbana.girar()))

print("Hibrida:" + str(hibrida.rin))
print("Comportamiento de la bicicleta hibrida: " + str(hibrida.avanzar()))


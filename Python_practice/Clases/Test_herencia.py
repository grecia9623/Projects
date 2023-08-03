class Animal:
    def comer(self):
        print("comiendo") 

class Perro(Animal):
    def pasear(self):
        print("paseando")

perro = Perro()
perro.comer()


class Chanchito(Perro):
    def programar(self):
        print("Programando")

chan = Chanchito()
chan.programar() #herencia multinivel SE RECOMIENDA QUE NO PASE DE 2 NIVELES

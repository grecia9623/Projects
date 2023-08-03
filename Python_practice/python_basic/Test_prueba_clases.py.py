
class Animal:
    def __int__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describir(self):
        print("Soy un animal de clase", type(self).__name__)

class Gato(Animal):
    def hablar(self):
        print("Miaw")

    # Polimorfismo usar una funcion/metodo que se llame igual,
    # de otra clase y puede variar el resultado
    def moverse(self):
        print("caminar en 4 patas")


class Perro(Animal):
    def hablar(self):
        print("Guau")

    def moverse(self):
        print("Caminando")

class Pez(Animal):
    def hablar(self):
        print("Glue")

    def moverse(self):
        print("Nadar")

hola = Perro.hablar("algo")
print(hola)
mi_gato = Gato.hablar("xxx")
mi_perro = Perro.hablar("xxx")
mi_pez = Pez.hablar("xxx")



class Ave: #CLASE PADRE
    def __init__(self):
        self.volador = "Volador" # antes era "TRUE"

    def vuela(self):
        print("Vuela ave")

class Pato(Ave): #SUBCLASE
    def __init__(self):
        super().__init__() #MANDAR LLAMAR AL CONSTRUCTOR DE LA CLASE PADRE
        self.nadar = "Nadador" # antes era "TRUE"

    def vuela(self):
        #super() ver los metodos de la clase padre
        print("Vuela pato")

pato = Pato()
pato.vuela()
print(pato.volador, pato.nadar)
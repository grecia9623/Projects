class Caminador:
    def caminar(self):
        print("caminando") 

class Voldador:
    def volar(self):
        print("volando")

class Nadador:
    def nadar(self):
        print("nadando")

class Pato(Voldador, Nadador, Caminador): 
#herencia de miltiples clases (NO REPETIR FUNCIONES EN LAS CLASES PORQUE PUEDE QUE TOME LA QUE NO ES)
    def programar(self):
        print("Programando")

chan = Pato()
chan.caminar()
chan.nadar()
chan.volar()
chan.programar()

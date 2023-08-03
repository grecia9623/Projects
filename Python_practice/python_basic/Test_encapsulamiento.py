#Encapsulamiento

class Empleado:
    def __init__(self,nombre,proyecto,salario):
        #atributos
        #por defecto los atributos son publicos y pueden acceder a ellos dentro de la clase o fuera de una clase
        self.nombre =nombre
        self.proyecto = proyecto
        #para que el atributo solo se acceda dentro de la clase y subclases se agrega un guion bajo antes del atributo
        self._proyecto = proyecto
        #self.salario = salario
        #para que sea un atributo privado se agregan dos guion bajo antes de definir el atributo
        self.__salario = salario #solo se podra acceder a el dentro de la clase

class Persona:
    def __init__(self,id,nombre,edad):
        self.__id = id
        self.nombre = nombre
        self.edad =edad

    def saludo(self):
        return "hola" + self.nombre
    def getIdentificacion(self):
        return self.__id
    def setIdentificacion(self,valor):
        self.__id = valor

persona1 = Persona(45678,"Jose",45)
persona1.setIdentificacion(12345)
#print(persona1._Persona__id) #para acceder a el atributo privado se
#agrego _nombreClase__nombreAtributoPriv
print(persona1.getIdentificacion())
print(persona1.nombre)
print(persona1.edad)
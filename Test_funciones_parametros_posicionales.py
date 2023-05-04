#funciones con parametros especiales o posicionales
"""
*args : se usan para pasar de forma opcional dististos valores
        son convencion, por lo que puede ir otro nombre pero * si es necesario
        ejemplo:
        def datos_usuario(*args):
            print(args)
        datos_usuario('Paola','Ramirez',24,'cra 56 #4 - 00','Cartagena'

**kwargs : Se usan para pasar distintos valores con la diferencia de que las variables tienen un nombre
         Se usa cuando se trabaja con base de datos, para filtrar informacion
        ejemplo
        def datos_usuario(**kwargs):
            print(kwargs)
        datos_usuario(nombre = 'Paola', apellido='Ramirez', edad=24, direccion='Cra 56 #4 - 00',
        ciudad='Cartagena')

Cuando se agregan mas de 3 argumentos arroja un error si no se hace por el modo *args

def suma(*operacion):
    s=0
    for i in operacion: #vamos a recorrer lo que tiene los parametros
        s += i
    return s

resultado = suma(25,125,4,36,78,45,781)
print(resultado)

def lenguaje(nombre, *lenguajes):
    print(f'Hola {nombre}')
    print(f'Tus lenguajes favoritos son: {lenguajes}')

lenguaje("Grecia","Python","Java","Ruby","Javascript")
#*args recibe los datos como una tupla
"""
def lenguaje(nombre, **kwargs):
    print(f'Hola {nombre}')
    print("Buscando informacion acerca de los lenguajes")
    print("Cargando informacion...\n")

    print("Información:")
    contador = 0
    print(type(kwargs))
    for clave in kwargs:
        contador += 1
        print(f'Tu {contador} lenguaje favorito es: {kwargs[clave]}')

lenguaje("Grecia",lenguaje1= "Python",lenguaje2="Java",lenguaje3= "Javascript", lenguaje4 ="Ruby")
#**kwargs recibe los datos en forma de diccionario
"""
try:
    n1 = int(input("Ingresa primer numero: "))
except:
    print("Ocurrio un error")
"""
#tipos de excepciones

"""
try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e: #todos los errores Exception
    print(type(e))
"""

try:
    n1 = int(input("Ingresa primer numero: "))
except ValueError as e: #solo el tipo de error ValueError
    print("Solo puedes ingresar numeros")
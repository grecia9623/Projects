

""" 
numero = 1
while numero < 100:
    print(numero)
    numero *= 2
"""
#------------------------------------------------
"""
comando = ""

while comando != "salir" and comando != "SALIR":
    comando = input("$ ")
    print(comando)
"""
#------------------------------------------------
"""
comando = ""

while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

"""
#----------------------Loops infinitos
"""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
"""    
#----------------------Loops anidados  (No es tan recomendable)
for j in range(3):  #outer for/loop
    for k in range(2): #inner for/loop
        print(f"{j}, {k}")
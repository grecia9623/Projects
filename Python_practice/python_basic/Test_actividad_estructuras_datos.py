
#print(f'Tu nombre es {nombre}')

agenda = {
    "Jose": 302944,
    "Mario": 829455,
    "Angel": 829405,
    "Luis": 930594,
}

consultando = True

while consultando:
    print("AGENDA")
    print("________________________________")
    print("1.Consultar\n2.Añadir\n3.Modificar\n4.Borrar\n5.Salir")

    opcion=""

    while opcion not in ("1","2","3","4","5"):
        opcion =input("Ingresa una opcion valida->")

        if opcion == "1":
            #pedir nombre
            nombre = input("Ingresa tu nombre completo: ")
            if nombre not in agenda:
                print(f'{nombre} no existe en la agenda')
            else:
                telefono = agenda[nombre]
                print(nombre,":", telefono)
        elif opcion == "2":
            #pedir nombre
            nombre = input("Ingresa tu nombre completo: ")
            #comprobar si existe
            if nombre in agenda:
                print(f"{nombre} ya existe")
            else:
                telefono =int(input("Ingrese su numero de celular: "))
                #añadir el telefono a la agenda
                agenda[nombre] = telefono
                print("El telefono se agrego correctamente")

        elif opcion == "3":
            # pedir nombre
            nombre = input("Ingresa tu nombre completo: ")
            if nombre not in agenda:
                print(f'{nombre} no existe en la agenda')
            else:
                telefono =int(input("Ingrese el nuevo numero de celular: "))
                #añadir el telefono a la agenda
                agenda[nombre] = telefono
                print("El telefono se modifico correctamente")

        elif opcion == "4":
            # pedir nombre
            nombre = input("Ingresa tu nombre completo: ")
            if nombre not in agenda:
                print(f'{nombre} no existe en la agenda')
            else:
                #borrar celular
                del agenda[nombre]
                print(f"El numero celular de {nombre} ha sido eliminado")

        elif opcion == "5":
            consultando = False
            print("Hasta pronto")
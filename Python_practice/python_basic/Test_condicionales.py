#actividad 2 Edutin academy
#Solicitar información
nombre = input("Ingrese el nombre del cliente: ")
valor_compra = float(input("Ingrese el valor de la compra: "))
#Establecer condiciones
if valor_compra < 80:
    print(f'Hola, {nombre}. El valor a pagar es: $ {valor_compra}')
elif 80 <= valor_compra < 150:
      descuento=0.1
elif 150 <= valor_compra <= 300:
      descuento=0.15
elif 300 < valor_compra < 500:
      descuento=0.2
print(f'Descuento aplicado: {descuento}')
descuento = valor_compra * descuento
precio_final = valor_compra - descuento
print(f'Compra sin descuento: {valor_compra} . Compra con descuento: {precio_final} Su descuento fue de: {descuento}')
#Angel 455 -> $364
#Rosa díaz 105 -> $94
#dilan gonzales 250 -> 212.5
#Kely Daza 430 -> $344
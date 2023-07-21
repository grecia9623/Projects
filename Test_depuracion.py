def largo(texto):
    resultado = 0
    for _ in texto: # Warning la variable para la iteracion char no se esta usando, se cambia por _
        resultado += 1
    return resultado
print("bandera")
l = largo("hola mundo")
print(l)
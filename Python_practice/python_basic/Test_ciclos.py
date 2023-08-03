#Actividad 3 edutin academy
#solicitar informacion
nombre = input("Nombre completo: ")
materias = 5
contador = 1
sumatoria = 0
while contador <= materias:
# hacer ciclo while, pedir datos, sumar la calificacion
    nombre_materia = input("Ingresa el nombre de la materia ("+ str(contador) +") de 5to semestre: ")
    calificacion = float(input("Calificacion obtenida en "+str(nombre_materia)+ ":"))
    sumatoria = sumatoria + calificacion#sumar la calificacion a la sumatoria
    contador = contador + 1 #Aumentar el contador para no hacer un ciclo infinito
#Hacer calculo e imprimir los resultados
promedio = sumatoria/materias
print("Promedio de 5to Semestre")
print(f'Hola, {nombre} tu promedio es {promedio}')
#Grecia Lopez promedio 4.26
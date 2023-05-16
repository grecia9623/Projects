import csv

# Abrir el archivo CSV
with open('C:/Users/M1GLOPEZSU/Desktop/Book1.csv', newline='') as csvfile:
    # Crear un objeto para leer el archivo CSV
    reader = csv.reader(csvfile, delimiter=',')

    # Copiar filas y columnas específicas
    filas = []
    for i, fila in enumerate(reader):
        if i >= 0 and i <= 27:  # Copia las filas
            # Copiar columnas A, B y C
            columnas = [fila[0], fila[1], fila[2]]
            # Reemplazar comillas simples y dobles en cada celda
            columnas_sin_comillas = [celda.replace("'", "").replace('"', '') for celda in columnas]
            filas.append(columnas_sin_comillas)

# Crear un archivo de texto
with open('resultado.txt', 'w') as f:
    # Iterar sobre las filas copiadas y escribirlas en el archivo de texto
    for fila in filas:
        # Convertir la fila a string y escribirla en el archivo de texto
        fila_str = ','.join(fila) + '")' '\n'
        f.write(f'print("{fila_str}')

with open('resultado.txt', 'r') as f, open("limpio.txt", "w") as output:
# Iterar sobre las filas copiadas y escribirlas en el archivo de texto
    for fila in f:
        # Convertir la fila a string y escribirla en el archivo de texto
        nuevo = fila.replace(",", " ")
        output.write(nuevo)

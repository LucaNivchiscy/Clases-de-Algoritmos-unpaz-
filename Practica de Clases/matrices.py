


"""
Ejercicio 4: Ceros en la contra-diagonal

Dada una matriz de 3x3 llena con el número 5, modificá la matriz de forma que la contra-diagonal (diagonal secundaria) 
contenga ceros y el resto de los elementos mantenga su valor original.

Ejercicio 5: Suma de filas y columnas

Solicitá al usuario que ingrese los valores de una matriz de 3x3. Luego, mostrá la matriz completa y calculá la suma de cada fila y de cada columna por separado.
Ejercicio 6: Buscaminas simplificado

Generá una matriz de 3x3 y colocá tres minas de forma aleatoria (representadas por el número 9). Luego, 
calculá cuántas minas hay alrededor de cada casilla no-minada, y completá el tablero con esos valores."""


import numpy as np
import random

TAM = 3
MINAS = 3

#Crear tablero con ceros
tablero = np.zeros((TAM, TAM), dtype=int)

#Colocar minas aleatorias (valor 9)
minas_colocadas = 0
while minas_colocadas < MINAS:
    i = random.randint(0, TAM-1)
    j = random.randint(0, TAM-1)
    if tablero[i][j] != 9:
        tablero[i][j] = 9
        minas_colocadas += 1

#Calcular números vecinos
for i in range(TAM):
    for j in range(TAM):
        if tablero[i][j] != 9:
            contador = 0
            for x in range(max(0, i-1), min(TAM, i+2)):
                for y in range(max(0, j-1), min(TAM, j+2)):
                    if tablero[x][y] == 9:
                        contador += 1
            tablero[i][j] = contador

print("Tablero (9 = mina):")
print(tablero)




















# matrix = np.full([3,3], 5)
#
# for i in range(3):
#     for j in range(3):
#         if i + j == 2:
#             matrix[i][j] = 0
#
# print(matrix)
#
#
#
# matrix = np.zeros([3,3])
# print(matrix)
#
# for i in range(3):
#     for j in range(3):
#         matrix[i][j] = int(input(f"Ingrese el cada valor de la matriz 3x3: "))
#
# print(matrix)
# suma_filas = 0
# suma_colum = 0
# for i in range(3):
#     suma_filas += matrix[i]
#
#
# for j in range(3):
#     suma_colum += matrix[:,j]
#
#
# print(suma_filas)
# print(suma_colum)
























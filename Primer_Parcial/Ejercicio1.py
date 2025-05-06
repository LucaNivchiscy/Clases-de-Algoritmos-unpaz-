import numpy as np
import random as ra

#creo la matriz con ceros
matrix = np.zeros([4,4])

#lleno la matriz con numeros randoms
for i in range(len(matrix)):
    for j in range(len(matrix)):
        num = ra.randint(10,100 )
        matrix[i][j] = num

for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end="\t")
    print()

#promedio de la diagonal
suma = 0
for suma_i in range(len(matrix)):
    for suma_j in range(len(matrix)):
        if suma_i == suma_j:
            suma = suma + matrix[suma_i][suma_i]
promedio = suma / 4

#cantidad de num pares en la parte inferior de la matriz
cont_pares = 0
for mayor_i in range(len(matrix)):
    for mayor_j in range(len(matrix)):
        if mayor_i > mayor_j:
            if matrix[mayor_i][mayor_j] % 2 == 0:
                cont_pares += 1


print(f"La cantidad de numeros pares en la parte inferior de la matriz es de: {cont_pares}")
print(f"el promedio de la diagonal principal de la matriz es: {promedio} ")










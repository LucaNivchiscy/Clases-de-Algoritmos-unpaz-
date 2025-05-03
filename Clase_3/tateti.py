import numpy as np

tamaño = 3

tablero = np.array([range(3), range(3), range(3)], dtype=str)
print(tablero)



def tablero():
    for i in range(tamaño):
        for j in range(tamaño):
            tablero[i][j] = "i"
        print(tablero)

tablero()



















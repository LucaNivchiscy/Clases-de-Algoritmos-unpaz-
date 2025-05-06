import random as ran
import array as arr
import numpy as np

"""

respuestas = arr.array("i", (ran.randint(1,10) for _ in range(40)))
print(respuestas)

for i in range(40):
    num_alt = ran.randint(1,10)
    respuestas.append(num_alt)
contador = 0
for i, nota in enumerate(respuestas):
    contador +=1
    print(f'calificacion nro{i +1}: {nota}')


for i in range(1,11):
    cantidad = 0
    for j in respuestas:
        if j == i:
            cantidad += 1
    print(cantidad)
#tipo de matrices e inicializarlas

matrix1 = np.array([[0,0,0], [0,0,0]])
print(matrix1)
matrix2 = np.zeros([2,3])
print(matrix2)
matrix3 = np.ones([2,3], dtype=int)
print(matrix3)
matrix4 = np.array([range(3),range(3)])
print("range:", matrix4)

matrix1 = np.matrix([range(3), range(3), range(3)])
print(matrix1)
print(matrix1[1,1])
matrix1[1,1] = 10
print(matrix1)

matrix2 = np.zeros([3,3])
for i in matrix2:
    for j in matrix2:
        if matrix2[1,1] == 0:
            matrix2[1,1]= 1

print(matrix2)
"""
"""matrix3 = np.array([range(3), range(3), range(3)])

for i in range(len(matrix3)):
    for j in range(len(matrix3):



print(matrix3)

"""



"""
matrix2[0]= 0
matrix2[1,0]= 0
matrix2[1,2]= 0
matrix2[2]= 0

"""













import numpy as np

matrix = np.array([range(3), range(3), range(3)])

matrix2 = np.array([range(3), range(3), range(3)])
print(matrix)



for i in range(len(matrix2)):
    for j in range(len(matrix2)):
        if i + j == (len(matrix2)) -1:
            matrix2[i][j] = 10
        else:
            matrix2[i][j] = 0

print(matrix2)












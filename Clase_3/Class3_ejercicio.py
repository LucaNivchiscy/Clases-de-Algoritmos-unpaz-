import numpy as np
import random as rn

dim = 5
matriz = np.array([range(dim), range(dim), range(dim), range(dim), range(dim)])


def menu():
    print("\tMENU\t\n1.cargar matriz manualmente \n2.Cargar la matriz de forma automatica \n3.mostrar matriz \n4.Modificar matriz \n5.mostrar el promedio de la diagonal principal \n6.Mostrar el menor de los numeros d la constradiagonal \n7.salir del programa \n-")
def menu1(matriz):
    print("llene la funcion con numeros por posicion: ")
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = int(input(f"num, para posicion {i}, {j} : " ))
    return matriz
#menu1 y menu2 se pueden unir
def menu2(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            matriz[i][j] = rn.randint(1,100)
    return matriz
def menu3(matriz):
    for i in range(dim):
        for j in range(dim):
            print(matriz [i][j], end="\t")
        print()



def menu4(matriz):
    fila = int(input("seleccione una fila: "))
    columna = int(input("seleccione una fila: "))
    nuevo_valor = int(input("ingrese nuevo valor: "))
    matriz[fila][columna] = nuevo_valor
#menu4 puede delegar la tarea a otra funcion de validar fila y columna

def menu5():
    suma = 0
    for i in range(dim):
        for j in range(dim):
            if i == j:
                suma += matriz[i][j]
    return suma / dim
while True:
    menu()
    opcion = int(input("elija una opcion: "))
    if opcion == 1:
        matriz = menu1(matriz)
    elif opcion == 2:
        matriz = menu2(matriz)
    elif opcion == 3:
        menu3(matriz)
    elif opcion == 4:
        menu4(matriz)
    elif opcion == 5:
        menu5()















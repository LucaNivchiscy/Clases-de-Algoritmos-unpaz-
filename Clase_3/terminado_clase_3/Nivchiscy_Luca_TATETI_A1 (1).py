#TATETI by Nivchiscy Luca
import numpy as np
from string import ascii_lowercase


#estructura (masomenos)
# Necesito crear el tablero:
    #dar el tamaño del tablero(previo)
# mostrar el tablero
#esto entra en un bucle:
    # solicitar ingresar una posicion
        # tanto a usuario X como usuario O
    # verificar que esa posicion es valida
    # rescribir esa posicion en caso de ser valida
        #hacerlo en base al tamaño del tablero
    # verificar un ganador
        #verificar por:
            #vertical
            #horizontal
            #diagonal
            #contra diagonal
# mostrar un ganador



#algunas variables
turno_actual = 0
ABC_string = ascii_lowercase





#crear y mostrar:
def mostrar_tablero(tablero):
    for i in tablero:
        for j in i:
            print(j, end=' ')
        print()

#arange:
#toma tipo de dato int, parecido a range toma como argumento; dato de inicio fin en este caso +1 para dar forma con reshape
#reshape:
#da la forma al vector en este caso 3*3
def crear_tablero_numeros():
    tablero = np.arange(1, TAM_TABLERO*TAM_TABLERO+1).reshape(TAM_TABLERO, TAM_TABLERO).astype(str)
    abc_tam = 0
    return tablero, abc_tam     #tengo que retornar abc_tam = 0 porque si ingreso una TAM_TABLERO = 3 revienta el codigo por los argumentos en solicitar_y_verificar_posicion(),


def crear_tablero_letras():
    abc_lista = []
    if TAM_TABLERO >= 6:
        for i in ABC_string:
            for j in ABC_string:
                abc_lista.append(i+j)
    elif TAM_TABLERO <=5:
        for i in ABC_string:
            abc_lista.append(i)
    abc_lista.insert(14,"ñ")    #me daba toc la ñ a lo ultimo
    abc_tam = abc_lista[:TAM_TABLERO*TAM_TABLERO]
    tablero = np.array(abc_tam).reshape(TAM_TABLERO, TAM_TABLERO)
    return tablero, abc_tam

#ABC_string = contiene todas las letras juntas
#abc_lista = esta vacia luego le hago un append de cada letra con un for
#abc_tam = es un array de letras hasta el numero del tablero * tablero
##################################################

#solicitar y rescribir por turnos:

#esta funcion retorna un numero valido dentro del tablero
def solicitar_y_verificar_posicion(TAM_TABLERO, abc_tam):
    while True:
        if TAM_TABLERO <= 3:
            posicion = input("Ingrese una posicion del 1-9: ")
            if posicion.isdigit():  #comprueba que el string contiene un digito, de ser asi es True
                posicion = int(posicion)
                if posicion >= 1 and posicion <= turnos_totales:
                    return str(posicion)
                else:
                    print("Debe ingresar una posicion entre 1-9")
            else:
                print("Ingrese un numero!")
        elif TAM_TABLERO > 3:
            posicion = input("Ingrese una letra de la cuadricula como posicion: ").lower()
            if posicion.isalpha():  #lo mismo que isdigit pero para letras epico
                for i in abc_tam:
                    if posicion == i:
                        return posicion
            else:
                print("Debe ingresar caracteres alfabeticos.")


#cuando itere y por ejemplo posicion = 5, tablero[i][j] = (1,1) itera hasta tal numero compara y remplaza.
def rescribir_posicion(tablero, posicion, marca):
    for i in range(TAM_TABLERO):
        for j in range(TAM_TABLERO):
            if tablero[i][j] == posicion:
                tablero[i][j] = marca
                return True
    #return False

def ganador(tablero):
    return ganador_diagonal_principal(tablero) or ganador_contra_diagonal(tablero)  or ganador_vertical(tablero)  or ganador_horizontal(tablero)


def ganador_diagonal_principal(tablero):
    contador_jugador_x = 0
    contador_jugador_o = 0
    for i in range(TAM_TABLERO):
        if tablero[i][i] == "X":    #i siempre tiene el mismo valor por lo que valida la diagonal principal
            contador_jugador_x += 1
        elif tablero[i][i] == "O":
            contador_jugador_o += 1
    if contador_jugador_x == consecutivos_p_ganar:
        print("Felicidades!")
        print("El Jugador X gano por diagonal principal!")
        return True
    if contador_jugador_o == consecutivos_p_ganar:
        print("Felicidades!")
        print("El Jugador O gano por diagonal principal!")
        return True
    return False

def ganador_contra_diagonal(tablero):
    contador_jugador_x = 0
    contador_jugador_o = 0
    for i in range(TAM_TABLERO):
        if tablero[i][TAM_TABLERO - i -1] == "X":   #primera iteracion 0,2 -> 1,1 -> 2,0 valida contra diagonal
            contador_jugador_x +=1
        elif tablero[i][TAM_TABLERO - i - 1]== "O":
            contador_jugador_o +=1
    if contador_jugador_x == consecutivos_p_ganar:
        print("Felicidades!")
        print("El Jugador X gano por la contra diagonal!")
        return True
    if contador_jugador_o == consecutivos_p_ganar:
        print("Felicidades!")
        print("El Jugador O gano por la contra diagonal!")
        return True
    return False

def ganador_vertical(tablero):
    for j in range(TAM_TABLERO):
        contador_jugador_x = 0  #se reinicia cuando termina el bucle i
        contador_jugador_o = 0
        for i in range(TAM_TABLERO):    #"itera" por columnas: 0,0 -> 1,0 -> 2,0 luego reinicia el contador y cambia de j
            if tablero[i][j] =="X":
                contador_jugador_x +=1
            elif tablero[i][j] == "O":
                contador_jugador_o +=1
        if contador_jugador_x == consecutivos_p_ganar:
            print("Felicidades!")
            print("El Jugador X gano por forma vertical!")
            return True
        if contador_jugador_o == consecutivos_p_ganar:
            print("Felicidades!")
            print("El Jugador O gano por forma vertical!")
            return True
    return False

def ganador_horizontal(tablero):
    for i in range(TAM_TABLERO):
        contador_jugador_x = 0
        contador_jugador_o = 0
        for j in range(TAM_TABLERO):
            if tablero[i][j] =="X":
                contador_jugador_x +=1
            elif tablero[i][j] == "O":
                contador_jugador_o +=1
        if contador_jugador_x == consecutivos_p_ganar:
            print("Felicidades!")
            print("El Jugador X gano por forma horizontal!")
            return True
        if contador_jugador_o == consecutivos_p_ganar:
            print("Felicidades!")
            print("El Jugador X gano por forma horizontal!")
            return True
    return False

def main(turno_actual, turnos_totales, tablero):
    print("-----TATETI-----")
    while True:
        mostrar_tablero(tablero)
        if ganador(tablero):   #esto devuelve true o false
            mostrar_tablero(tablero)
            break
        elif turnos_totales == 0:
            print("Es un empate!")
            break
        elif turno_actual == 0:
            print("Turno del jugador 1")
            marca = "X"
            pos = solicitar_y_verificar_posicion(TAM_TABLERO, abc_tam)
            if rescribir_posicion(tablero, pos, marca):
                turno_actual = 1 - turno_actual
                turnos_totales -=1
                continue
            else:
                print("Posicion ocupada")
                print()
                continue
        else:
            print("Turno jugador 2")
            marca = "O"
            pos = solicitar_y_verificar_posicion(TAM_TABLERO, abc_tam)
            if rescribir_posicion(tablero, pos, marca):
                turno_actual = 1 - turno_actual
                turnos_totales -=1
                continue
            else:
                print("Posicion ocupada")
                print()
                continue

#Ejecucion del juego
while True:
    jugar = input("Desea jugar? (s/n): ").lower()
    if jugar == "s":
        TAM_TABLERO = int(input("Ingrese el tamaño del tablero: "))
        turnos_totales = (TAM_TABLERO * TAM_TABLERO)
        while True:
            consecutivos_p_ganar = int(input("Cuantas fichas consecutivas desea para ganar?: "))
            if consecutivos_p_ganar <= TAM_TABLERO:
                break
            else:
                print(f"Ingrese una cantidad igual o menor a {TAM_TABLERO}")
        if TAM_TABLERO <= 3 and TAM_TABLERO >=1:
            tablero, abc_tam = crear_tablero_numeros()
        else:
            tablero, abc_tam = crear_tablero_letras()
        main(turno_actual,turnos_totales, tablero)
    elif jugar == "n":
        print("Gracias por jugar!")
        break
    else:
        print("Ingrese s(si) o n(no)")





#favor de no comprobar con turnos_totales menores al TAM_TABLERO u.u
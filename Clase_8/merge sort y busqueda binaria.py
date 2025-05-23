lista_de_numeros = [14, 7, 3, 12, 9, 11, 6, 2]


#merge sort
def merge_sort(lista, lista_temp, inicio, fin):

    if inicio < fin:
        medio = (inicio+fin) // 2
        merge_sort(lista, lista_temp, inicio, medio)
        merge_sort(lista, lista_temp, medio + 1, fin)
        merge(lista, lista_temp, inicio, medio +1, fin)

def merge(lista, lista_temp, inicio, medio, fin):
    fin_primera_parte = medio -1 #fin de la lista izquierda
    indice_temp = inicio #
    tamano_de_lista = fin -inicio +1
    while inicio <= fin_primera_parte and medio <= fin:
        if lista[inicio] >= lista[medio]:
            lista_temp[indice_temp]= lista[inicio]
            inicio +=1
        else:
            lista_temp[indice_temp] = lista[medio]
            medio +=1
        indice_temp +=1
    while inicio <= fin_primera_parte:
        lista_temp[indice_temp]= lista[inicio]
        indice_temp +=1
        inicio +=1
    while medio <= fin:
        lista_temp[indice_temp] = lista[medio]
        indice_temp +=1
        medio +=1
    for i in range(0, tamano_de_lista):
        lista[fin] = lista_temp[fin]
        fin -=1

def main(lista_de_numeros):
    tam_de_lista = len(lista_de_numeros)
    lista_temp = [0] * tam_de_lista
    merge_sort(lista_de_numeros, lista_temp, 0, tam_de_lista-1)
    for n in lista_de_numeros:
        print(n)
        # for i in range(len(lista_de_numeros), 0, -1):
        #     if n == lista_de_numeros[i-1]:
        #         print(n)

main(lista_de_numeros)


#Busqueda Binaria
def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista) -1
    while izq <= der:
        medio = (izq+der) // 2
        if lista[medio] == x:
            return x
        elif lista[medio] > x:
            der = medio -1
        else:
            izq = medio +1
    return False

def buscar(dato):
    if not dato:
        print("el numero no existe en la lista")
        return
    print("numero encontrado")

dato = busqueda_binaria(lista_de_numeros, 2)

buscar(dato)
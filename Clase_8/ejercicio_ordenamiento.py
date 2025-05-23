"""
V1
En un establecimiento educativo se desea realizar un cálculo estadístico y para ello se ingresan los
siguientes datos por alumno:
    Número de legajo
    Nombre y Apellido
    Promedio de calificaciones
Se desea obtener un listado ordenado por promedio en forma descendente de todos aquellos alumnos
    cuyo promedio supere o iguale el promedio general.
Realicen el procedimiento con un listado de 10 alumnos cuyos valores queden escritos directamente en el código
V2
Tomar como base de código el ejercicio anterior de ordenamiento de alumnos.
Modificar la estructura del alumno para que en lugar de tener un promedio de notas pueda tener una lista de notas con una cantidad máxima de 5 notas. 
Agregar un menú con las siguientes opciones:
    1. Crear alumno (no se puede tener dos alumnos con el mismo legajo. La escala de notas es de 1 a 10 incluyendo decimales)
    2. Agregar notas a alumno. Permite agregarle notas al alumno siempre que no se supere el limite
    3. Ver alumnos. Debe listar todos los alumnos con su legajo, nombre y promedio de notas
    4. Mostrar alumnos que superan promedio general ordenados de forma descendente
    5. Mostrar alumnos que superan promedio general ordenados de forma ascendente
"""


class Alumno:
    def __init__(self, legajo: int, nombre: str, apellido: str, promedio: float):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.promedio = promedio
        self.notas = []

    def __str__(self):
        return f"Legajo: {self.legajo}, Nombre: {self.nombre}, Apellido: {self.apellido}, Promedio: {self.promedio}"


class GestorAlumnos:
    def __init__(self):
        self.alumnos: list[Alumno] = []

#Funciones internas
    def _generar_num_legajo(self):
        nro = self._entero_positivo("Ingrese el legajo del alumno: ")
        for alumno in self.alumnos:
            if alumno.legajo == nro:
                print("El legajo ya existe.")
                return self._generar_num_legajo()
        return nro

    def _entero_positivo(self, mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor < 0:
                    raise ValueError
                return valor
            except ValueError:
                print("Por favor, ingrese un número entero positivo.")

    def _nota_valida(self, mensaje):
        while True:
            try:
                nota = float(input(mensaje))
                if 1.0 <= nota <= 10.0:
                    return nota
                else:
                    print("La nota debe estar entre 1 y 10.")
            except ValueError:
                print("Por favor, ingrese un número válido (decimal permitido).")

    def _buscar_legajo(self):
        legajo = self._entero_positivo("Ingrese el legajo del alumno: ")
        for alumno in self.alumnos:
            if alumno.legajo == legajo:
                return alumno
        return None

    def _promedio_alumno(self, alumno):
        if alumno.notas:
            alumno.promedio = sum(alumno.notas) / len(alumno.notas)
        else:
            alumno.promedio = 0

    def _promedio_general(self):
        promedios = [alumno.promedio for alumno in self.alumnos if alumno.promedio > 0]
        if not self.alumnos:
            return 0
        return sum(promedios) / len(promedios)

#Funcion interna de ordenamiento
    def _merge_sort(self,lista, lista_temp, inicio, fin, asc: bool):

        if inicio < fin:
            medio = (inicio + fin) // 2
            self._merge_sort( lista, lista_temp, inicio, medio, asc)
            self._merge_sort(lista, lista_temp, medio + 1, fin, asc)
            self._merge(lista, lista_temp, inicio, medio + 1, fin, asc)

    def _merge(self, lista, lista_temp, inicio, medio, fin, asc: bool):
        fin_primera_parte = medio - 1  # fin de la lista izquierda
        indice_temp = inicio
        tamano_de_lista = fin - inicio + 1
        while inicio <= fin_primera_parte and medio <= fin:
            if (asc and lista[inicio].promedio <= lista[medio].promedio) or (not asc and lista[inicio].promedio >= lista[medio].promedio):
                lista_temp[indice_temp] = lista[inicio]
                inicio += 1
            else:
                lista_temp[indice_temp] = lista[medio]
                medio += 1
            indice_temp += 1
        while inicio <= fin_primera_parte:
            lista_temp[indice_temp] = lista[inicio]
            indice_temp += 1
            inicio += 1
        while medio <= fin:
            lista_temp[indice_temp] = lista[medio]
            indice_temp += 1
            medio += 1
        for i in range(0, tamano_de_lista):
            lista[fin] = lista_temp[fin]
            fin -= 1

    def _main(self, lista_de_alumnos, asc: bool):
        temp = lista_de_alumnos.copy()
        lista_temp = [0] * len(temp)
        self._merge_sort(temp , lista_temp, 0, len(lista_de_alumnos) - 1, asc)
        return temp

#funciones de la clase

    def agregar_alumno(self):
        legajo = self._generar_num_legajo()
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        promedio = 0
        nuevo_alumno = Alumno(legajo, nombre, apellido, promedio)
        self.alumnos.append(nuevo_alumno)
        print(f"Alumno {nombre} {apellido} agregado con legajo {legajo}.")

    def agregar_nota(self):
        alumno_encontrado = self._buscar_legajo()
        if not alumno_encontrado:
            print("El legajo no existe.")
            return
        if len(alumno_encontrado.notas) >= 5:
            print("El alumno ya tiene 5 notas.")
            return
        nota = self._nota_valida("Ingrese la nota del alumno (1 a 10): ")
        if nota < 1 or nota > 10:
            print("La nota debe estar entre 1 y 10.")
            return
        alumno_encontrado.notas.append(nota)
        self._promedio_alumno(alumno_encontrado)
        print(f"Nota {nota} agregada al alumno {alumno_encontrado.nombre} {alumno_encontrado.apellido}.")

    def mostrar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return
        print("Lista de alumnos:")
        for alumno in self.alumnos:
            print(alumno)


    def mostrar_alumnos_superan_promedio(self, asc):
        if not self.alumnos:
            print("No hay alumnos registrados.")
            return
        promedio_general = self._promedio_general()
        print(f"Promedio general: {promedio_general}")
        alumnos_superan = [alumno for alumno in self.alumnos if alumno.promedio >= promedio_general]
        if not alumnos_superan:
            print("No hay alumnos que superen el promedio general.")
            return
        ordenados = self._main(alumnos_superan, asc)
        print("Alumnos que superan el promedio general:")
        for alumno in ordenados:
            print(alumno)

#Menu
def menu():
    gestor = GestorAlumnos()
    while True:
        print("\nMenu:")
        print("1. Crear alumno")
        print("2. Agregar notas a alumno")
        print("3. Ver alumnos")
        print("4. Mostrar alumnos que superan promedio general (descendente)")
        print("5. Mostrar alumnos que superan promedio general (ascendente)")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            gestor.agregar_alumno()
        elif opcion == "2":
            gestor.agregar_nota()
        elif opcion == "3":
            gestor.mostrar_alumnos()
        elif opcion == "4":
            gestor.mostrar_alumnos_superan_promedio(False)
        elif opcion == "5":
            gestor.mostrar_alumnos_superan_promedio(True)
        elif opcion == "6":
            break
        else:
            print("Opción inválida, intente nuevamente.")





menu()





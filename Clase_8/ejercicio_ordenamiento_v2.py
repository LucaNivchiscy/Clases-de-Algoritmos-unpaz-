class Alumno:
    def __init__(self, legajo: int, nombre: str, apellido: str, promedio: float):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        self.promedio = promedio
        self.notas = []

    def __str__(self):
        return f"Legajo: {self.legajo} | Nombre: {self.nombre} {self.apellido} | Promedio: {self.promedio:.2f}"


class GestorAlumnos:
    def __init__(self):
        self.alumnos: list[Alumno] = []

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

    def _buscar_legajo(self):
        legajo = self._entero_positivo("Ingrese el legajo del alumno: ")
        for alumno in self.alumnos:
            if alumno.legajo == legajo:
                return alumno
        return None

    def _promedio_alumno(self, alumno):
        if alumno.notas:
            alumno.promedio = sum(alumno.notas) / len(alumno.notas)

    def _promedio_general(self):
        promedios = [alumno.promedio for alumno in self.alumnos if alumno.promedio > 0]
        if not promedios:
            return 0
        return sum(promedios) / len(promedios)

    def _merge_sort(self, lista, lista_temp, inicio, fin, asc: bool):
        if inicio < fin:
            medio = (inicio + fin) // 2
            self._merge_sort(lista, lista_temp, inicio, medio, asc)
            self._merge_sort(lista, lista_temp, medio + 1, fin, asc)
            self._merge(lista, lista_temp, inicio, medio + 1, fin, asc)

    def _merge(self, lista, lista_temp, inicio, medio, fin, asc: bool):
        fin_primera_parte = medio - 1
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

        for i in range(tamano_de_lista):
            lista[fin] = lista_temp[fin]
            fin -= 1

    def _main(self, lista_de_alumnos, asc: bool):
        temp = lista_de_alumnos.copy()
        lista_temp = [0] * len(temp)
        self._merge_sort(temp, lista_temp, 0, len(lista_de_alumnos) - 1, asc)
        return temp

    def agregar_alumno(self):
        legajo = self._generar_num_legajo()
        nombre = input("Ingrese el nombre del alumno: ").capitalize()
        apellido = input("Ingrese el apellido del alumno: ").capitalize()
        promedio = 0
        nuevo_alumno = Alumno(legajo, nombre, apellido, promedio)
        self.alumnos.append(nuevo_alumno)
        print(f"\n✅ Alumno {nombre} {apellido} agregado con legajo {legajo}.\n")

    def agregar_nota(self):
        alumno_encontrado = self._buscar_legajo()
        if not alumno_encontrado:
            print("❌ El legajo no existe.")
            return
        print(f"\n📝 Agregando notas al alumno: {alumno_encontrado.nombre} {alumno_encontrado.apellido}")
        while len(alumno_encontrado.notas) < 5:
            nota_input = input(f"Ingrese una nota (1-10) o 's' para salir [Notas actuales: {alumno_encontrado.notas}]: ")
            if nota_input.lower() == 's':
                break
            try:
                nota = float(nota_input)
                if 1 <= nota <= 10:
                    alumno_encontrado.notas.append(nota)
                    self._promedio_alumno(alumno_encontrado)
                    print(f"✅ Nota {nota} agregada.")
                else:
                    print("❌ La nota debe estar entre 1 y 10.")
            except ValueError:
                print("❌ Entrada no válida. Intente de nuevo.")
            if len(alumno_encontrado.notas) == 5:
                print("⚠️ El alumno ya tiene 5 notas.")
                break

    def mostrar_alumnos(self):
        if not self.alumnos:
            print("📭 No hay alumnos registrados.")
            return
        print("\n📋 Lista de alumnos:")
        for alumno in self.alumnos:
            print(alumno)

    def mostrar_alumnos_superan_promedio(self, asc):
        if not self.alumnos:
            print("📭 No hay alumnos registrados.")
            return
        promedio_general = self._promedio_general()
        print(f"\n📈 Promedio general: {promedio_general:.2f}")
        alumnos_superan = [alumno for alumno in self.alumnos if alumno.promedio >= promedio_general]
        if not alumnos_superan:
            print("❌ No hay alumnos que superen el promedio general.")
            return
        ordenados = self._main(alumnos_superan, asc)
        print("\n🎓 Alumnos que superan el promedio general:")
        for alumno in ordenados:
            print(alumno)


def menu():
    gestor = GestorAlumnos()
    while True:
        print("\n" + "=" * 50)
        print("🎓 MENÚ DE GESTIÓN DE ALUMNOS".center(50))
        print("=" * 50)
        print("1️⃣  Crear alumno")
        print("2️⃣  Agregar notas a alumno")
        print("3️⃣  Ver todos los alumnos")
        print("4️⃣  Mostrar alumnos que superan el promedio (descendente)")
        print("5️⃣  Mostrar alumnos que superan el promedio (ascendente)")
        print("6️⃣  Salir")
        print("=" * 50)
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
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción inválida. Intente nuevamente.")


# Ejecutar el menú
menu()

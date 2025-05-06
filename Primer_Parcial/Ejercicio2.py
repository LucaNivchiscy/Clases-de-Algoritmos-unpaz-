

class Curso:
    def __init__(self, id: int, nombre: str, descripcion: str, horas: int, categoria: str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.horas = horas
        self.categoria = categoria


    def __str__(self):
        return f"ID del Curso: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}, Cantidad de Horas: {self.horas}, Categoria: {self.categoria}"

class GestorCursos:
    def __init__(self):
        self.cursos: list[Curso] = []
        self.MAX = 10
        self.cont = 0

    def cargar_curso(self):
        if len(self.cursos) <= 10:
            id = self._generar_id_curso()
            nombre = input("ingrese un nombre para el curso: ")
            descripcion = input("ingrese una descripcion para el curso: ")
            horas = self._validar_horas()
            categoria = input("defina una categoria para el curso: ")
            nuevo_curso = Curso(id, nombre, descripcion, horas, categoria)
            self.cursos.append(nuevo_curso)
            print("Curso Creado.")
            input("presione enter para continuar")

        else:
            print(f"Cantidad maxima de cursos alcanzada, maximo:{self.MAX}")
            return


    def _validar_horas(self):
        horas = int(input("ingrese la cantidad de horas de duracion del curso: "))
        while True:
            if horas <= 0:
                print("La hora ingresada no es valida.")
                continue
            if horas > 0:
                return horas

    def _generar_id_curso(self):
        """Genera un id de curso único"""
        if not self.cursos:
            return 1
        return max(curso.id for curso in self.cursos) + 1

    def mostrar_cursos(self):
        if not self._verificar_si_hay_cursos():
            return
        for curso in self.cursos:
            print(curso)

    def curso_mayor_duracion(self):
        if not self._verificar_si_hay_cursos():
            return
        h = 0
        curso_mas_largo = []
        for curso in self.cursos:
            if h < curso.horas:
                h = curso.horas
                curso_mas_largo = curso
        print(f"el curso mas largo es: {curso_mas_largo}")

    def verificar_id(self, id):
        if not self._verificar_si_hay_cursos():
            return
        for curso in self.cursos:
            if curso.id == id:
                return curso
        return None

    def buscar_curso_por_codigo(self, id):
        if not self._verificar_si_hay_cursos():
            return
        curso = self.verificar_id(id)
        if not curso:
            print("Curso no encontrado.")
            return
        print(curso)

    def _verificar_si_hay_cursos(self):
        if not self.cursos:
            print("No hay cursos cargados.")
            return False
        return True


class Menu:
    def __init__(self):
        self.menu = [
            "1. Cargar Curso",
            "2. Mostrar Todos los cursos cargados",
            "3. Informar el curso de mayor duracion",
            "4. Buscar curso por codigo",
            "5. Salir"
        ]

    def mostrar_menu(self):
        print("Menu de Opciones:")
        for i in self.menu:
            print(i)

    def opcion_selecionada(self):
        opcion = input("seleccione una opcion: ")
        return opcion


class Aplicacion:
    def __init__(self):
        self.gestor_cursos = GestorCursos()
        self.menu = Menu()

    """[
        "1. Cargar Curso",
        "2. Mostrar Todos los cursos cargados",
        "3. Informar el curso de mayor duracion",
        "4. Buscar curso por codigo",
        "5. Salir"
    ]"""
    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            opcion = self.menu.opcion_selecionada()
            if opcion == '1':
                self.gestor_cursos.cargar_curso()
            elif opcion == '2':
                self.gestor_cursos.mostrar_cursos()
            elif opcion == '3':
                self.gestor_cursos.curso_mayor_duracion()
            elif opcion == '4':
                self.gestor_cursos.buscar_curso_por_codigo(int(input("ingrese la id del curso: ")))
            elif opcion == '5':
                print("saliendo del programa...")
                break
            else:
                print("la opcion ingresada no es valida intente otra vez")


app = Aplicacion()
app.ejecutar()












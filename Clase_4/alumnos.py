"""
Desarrollar mediante código de programación la carga de datos de alumnos y que posea la siguiente estructura:

Codigo_Alumno (numerico autoincremental)
Apellido y Nombre (string)
Telefono (string)
Fecha de nacimiento (tipo Fecha)

Para ello deberá utilizar un menú con las siguientes opciones:

Crear nuevo alumno
Modificar alumno
Eliminar alumno
Ver alumnos
Buscar alumno por Codigo de Alumno
Salir del programa
Se deja como base la clase Fecha para que puedan reutilizarla,
tener en cuenta que para crear una nueva fecha deben pasarle al constructor un formato de fecha válido "dd/mm/AAAA" donde dd representa el día,
mm el mes y AAAA el año:"""

import re
from datetime import datetime




class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError('Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


class Alumno:
    def __init__(self, id: int, nombre: str, apellido: str, telefono: str, fecha_nacimiento: Fecha):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Apellido: {self.apellido}, Telefono: {self.telefono}, Fecha de Nacimiento: {self.fecha_nacimiento}"


class Menu:
    def __init__(self, opciones: list):
        self.opciones_menu = opciones

    def mostrar_menu(self):
        for op in self.opciones_menu:
            print(op)

    def opcion_seleccionada(self):
        print("Bienvenido al sistema de gestion de alumnos")
        opciones = input('elegir opcion:')
        return opciones





class GestionarAlumnos:
    def __init__(self):
        self.alumnos: list[Alumno] = []

    def _crear_id(self):
        if not self.alumnos:
            return 1
        return max(a.id for a in self.alumnos) + 1 #max([1,2,3]) = 3


    def crear_alumno(self):
        id = self._crear_id()
        nombre = input("ingrese un nombre: ").capitalize()
        apellido = input("ingrese un apellido: ").capitalize()
        telefono = input("ingrese un telefono: ")
        fecha_str = input("ingrese una fecha de nacimiento (dd/mm/aaaa): ")
        fecha = Fecha(fecha_str)
        nuevo_alumno = Alumno(id, nombre, apellido, telefono, fecha)
        self.alumnos.append(nuevo_alumno)

    def buscar_alumno_por_codigo(self,id):
        for alumno in self.alumnos:
            if alumno.id == id:
                return alumno
        return False

    def alumno_por_codigo(self, id):
        alumno_codigo = self.buscar_alumno_por_codigo(id)
        if alumno_codigo:
            print(alumno_codigo)


    def modificar_alumno(self,id):
        alumno = self.buscar_alumno_por_codigo(id)
        if not alumno:
            return 'Alumno no existente'
        nombre = input("ingrese un nombre: ").capitalize()
        apellido = input("ingrese un apellido: ").capitalize()
        telefono = input("ingrese un telefono: ")
        fecha_str = input("ingrese una fecha de nacimiento (dd/mm/aaaa): ")
        fecha = Fecha(fecha_str)
        if nombre: alumno.nombre = nombre
        if apellido: alumno.apellido = apellido
        if telefono: alumno.telefono = telefono
        if fecha: alumno.fecha_nacimiento = fecha

    def eliminar_alumno(self, id):
        alumno = self.buscar_alumno_por_codigo(id)
        if not alumno:
            return 'Alumno no existente'
        self.alumnos.remove(alumno)

    def mostrar_alumnos(self):
        for alumno in self.alumnos:
            print(alumno)


class Aplicacion:
    def __init__(self):
        self.gestor = GestionarAlumnos()

    def ejecutar(self):
        """["1. Crear nuevo alumno", "2. Ver alumnos", "3. Buscar alumno por Codigo de Alumno", "4. Modificar Alumnos",
         "5. Eliminar alumno", "6. Salir"]"""
        while True:
            menu = Menu( ["1. Crear nuevo alumno","2. Ver alumnos","3. Buscar alumno por Codigo de Alumno","4. Modificar Alumnos","5. Eliminar alumno","6. Salir"])
            menu.mostrar_menu()
            opcion_elegida = menu.opcion_seleccionada()
            if opcion_elegida == "1":
                self.gestor.crear_alumno()
            elif opcion_elegida == '2':
                self.gestor.mostrar_alumnos()
            elif opcion_elegida == "3":
                id = int(input("ingrese un id: "))
                self.gestor.alumno_por_codigo(id)
            elif opcion_elegida == "4":
                id = int(input("ingrese un id: "))
                self.gestor.modificar_alumno(id)
            elif opcion_elegida == "5":
                id = int(input("ingrese un id: "))
                self.gestor.eliminar_alumno(id)
            elif opcion_elegida == "6":
                print("chau")
                break
            else:
                print("opcion invalida")



app = Aplicacion()
app.ejecutar()




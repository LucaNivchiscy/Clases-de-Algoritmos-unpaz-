from fecha import Fecha
from paciente import Paciente
import os
import pickle



class GestionDePacientes:
    def __init__(self, archivo_pacientes: str, gestion_de_turnos: 'GestionDeTurnos'=None):
        self.archivo_pacientes = archivo_pacientes
        self.pacientes: list[Paciente] = self._cargar_pacientes()
        self.gestion_de_turnos = gestion_de_turnos
#--------------------------------FUNCIONES PRIVADAS--------------------------------#
    def _cargar_pacientes(self) -> list[Paciente]:
        if not os.path.exists(self.archivo_pacientes):
            return []
        try:
            with open(self.archivo_pacientes, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar_pacientes(self):
        with open(self.archivo_pacientes, "wb") as f:
            pickle.dump(self.pacientes, f)

    def _validar_dni(self, mensaje: str = "Ingrese el DNI del paciente ('s' para salir): ") -> str | None:
        while True:
            dni = input(mensaje).strip()
            if dni.lower() == 's':
                print("Operación cancelada.")
                return None
            if dni.isdigit() and len(dni) >= 7:
                return dni
            print("DNI inválido. Debe ser numérico y tener al menos 7 dígitos.")

    def _encontrar_paciente_por_dni(self, dni: str, mensaje=True) -> Paciente | None:
        for paciente in self.pacientes:
            if paciente.DNI == dni:
                return paciente
        if mensaje:
            print(f"No se encontró un paciente con DNI {dni}.")
        return None

#--------------------------------FUNCIONES PÚBLICAS--------------------------------#
    def listar_pacientes(self):
        if not self.pacientes:
            print("No hay pacientes registrados.")
            return
        print("Lista de Pacientes:")
        for paciente in self.pacientes:
            print(paciente)

    def buscar_paciente(self):
        dni = self._validar_dni()
        if not dni:
            return
        paciente = self._encontrar_paciente_por_dni(dni)
        if not paciente:
            return
        print(paciente)

    def agregar_paciente(self):
        while True:
            dni = self._validar_dni()
            if not dni:
                return
            if self._encontrar_paciente_por_dni(dni, mensaje=False):
                print(f"Ya existe un paciente con DNI {dni}.")
                continue
            break
        nombre = input("Ingrese el nombre del paciente: ").strip().title()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        while True:
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
            try:
                fecha_nacimiento = Fecha(fecha_nacimiento)
                break
            except ValueError as e:
                print(f"Error al crear la fecha: {e}. Por favor, intente nuevamente.")

        obra_social = input("Ingrese la obra social del paciente (o presione enter para no agregar nada): ").strip().upper() or "No Tiene obra social"
        nuevo_paciente = Paciente(dni, nombre, fecha_nacimiento, obra_social)
        self.pacientes.append(nuevo_paciente)
        self._guardar_pacientes()
        print(f"Paciente {nombre} agregado exitosamente.")

    def modificar_paciente(self):
        dni = self._validar_dni()
        if not dni:
            return
        paciente = self._encontrar_paciente_por_dni(dni)
        if not paciente:
            return
        print(paciente)
        nombre = input("Ingrese el nuevo nombre del paciente (o presione enter para no modificar): ").strip().title() or paciente.nombre
        fecha_nacimiento_str = input("Ingrese la nueva fecha de nacimiento (dd/mm/aaaa) (o presione enter para no modificar): ").strip() or str(paciente.fecha_nacimiento)
        try:
            fecha_nacimiento = Fecha(fecha_nacimiento_str)
        except ValueError as e:
            print(f"Error al crear la fecha: {e}")
            return
        obra_social = input("Ingrese la nueva obra social del paciente (o presione enter para no modificar): ").strip() or paciente.obra_social
        paciente.nombre = nombre
        paciente.fecha_nacimiento = fecha_nacimiento
        paciente.obra_social = obra_social
        self._guardar_pacientes()
        print(f"Paciente {paciente.nombre} modificado exitosamente.")

    def eliminar_paciente(self):
        dni = self._validar_dni()
        if not dni:
            return
        paciente = self._encontrar_paciente_por_dni(dni)
        if not paciente:
            return
        confirmacion = input(f"¿Está seguro de que desea eliminar al paciente {paciente.nombre}? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.pacientes.remove(paciente)
            self._guardar_pacientes()
            if self.gestion_de_turnos:
                for turno in self.gestion_de_turnos.turnos:
                    if turno.paciente.DNI == paciente.DNI:
                        self.gestion_de_turnos.turnos.remove(turno)
                self.gestion_de_turnos._guardar_turnos()
            print(f"Paciente {paciente.nombre} eliminado exitosamente.")
        else:
            print("Operación cancelada.")

    def guardar_cambios(self):
        self._guardar_pacientes()
        print("Cambios guardados exitosamente.")
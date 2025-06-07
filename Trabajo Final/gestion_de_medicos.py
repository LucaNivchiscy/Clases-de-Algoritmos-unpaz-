from medico import Medico
import os
import pickle


class GestionDeMedicos:
    def __init__(self, archivo_medicos: str, gestion_de_turnos: 'GestionDeTurnos'=None):
        self.archivo_medicos = archivo_medicos
        self.medicos: list[Medico] = self._cargar_medicos()
        self.gestion_de_turnos = gestion_de_turnos

#--------------------------------FUNCIONES PRIVADAS--------------------------------#
    def _cargar_medicos(self) -> list[Medico]:
        if not os.path.exists(self.archivo_medicos):
            return []
        try:
            with open(self.archivo_medicos, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar_medicos(self):
        with open(self.archivo_medicos, "wb") as f:
            pickle.dump(self.medicos , f)

    def _validar_matricula(self, mensaje: str= "Ingrese la matrícula del médico ('s' para cancelar): ") -> str | None:
        while True:
            matricula = input(mensaje).strip()
            if matricula.lower() == 's':
                print("Operación cancelada.")
                return None
            if matricula.isdigit() and len(matricula) >= 5:
                return matricula
            print("Matrícula inválida. Debe ser numérica y tener al menos 5 dígitos.")

    def _validar_str(self, mensaje: str) -> str:
        while True:
            nombre = input(mensaje).strip().title()
            if not nombre:
                print("El nombre no puede estar vacío.")
                continue
            if nombre:
                return nombre
            print("Ingrese el dato requerido.")

    def _encontrar_medico_por_matricula(self, matricula, mensaje: bool= True) -> Medico | None:
        for medico in self.medicos:
            if medico.matricula == matricula:
                return medico
        if mensaje:
            print(f"No se encontró un médico con matrícula {matricula}.")
        return None



#--------------------------------FUNCIONES PÚBLICAS--------------------------------#
    def listar_medicos(self):
        if not self.medicos:
            print("No hay medicos registrados.")
            return
        print("Lista de Médicos:")
        for medico in self.medicos:
            print(medico)

    def buscar_medico(self):
        matricula = self._validar_matricula()
        if not matricula:
            return
        medico = self._encontrar_medico_por_matricula(matricula)
        if not medico:
            return
        print(f"Médico encontrado: {medico}")

    def agregar_medico(self):
        while True:
            control = input("¿Desea registrar un nuevo médico? (s/n): ").strip().lower()
            if control == 'n':
                print("Operación cancelada.")
                return
            matricula = self._validar_matricula()
            if not matricula:
                return
            if self._encontrar_medico_por_matricula(matricula, mensaje=False):
                print(f"Ya existe un médico con matrícula {matricula}.")
                continue
            break
        if not matricula:
            return

        nombre = self._validar_str("Ingrese el nombre del médico: ")
        especialidad = self._validar_str("Ingrese la especialidad del médico: ")
        nuevo_medico = Medico(matricula, nombre, especialidad)
        self.medicos.append(nuevo_medico)
        self._guardar_medicos()
        print(f"Médico {nombre} agregado exitosamente.")

    def modificar_medico(self):
        matricula = self._validar_matricula()
        if not matricula:
            return
        medico = self._encontrar_medico_por_matricula(matricula)
        if not medico:
            return
        print(f"Datos actuales del médico: {medico}")
        nombre = input("Ingrese el nuevo nombre del médico (o presione enter para no modificar): ").strip().title() or medico.nombre
        especialidad = input("Ingrese la nueva especialidad del médico (o presione enter para no modificar): ").strip().title() or medico.especialidad
        medico.nombre = nombre
        medico.especialidad = especialidad
        self._guardar_medicos()
        print(f"Médico {medico.nombre} modificado exitosamente.")

    def eliminar_medico(self):
        matricula = self._validar_matricula("Ingrese la matrícula del médico a eliminar ('s' para salir): ")
        if not matricula:
            return
        medico = self._encontrar_medico_por_matricula(matricula)
        if not medico:
            return
        confirmacion = input(f"¿Está seguro de que desea eliminar al médico {medico.nombre}? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.medicos.remove(medico)
            self._guardar_medicos()
            if self.gestion_de_turnos:
                turnos = []
                for turno in self.gestion_de_turnos.turnos:
                    if turno.medico.matricula != medico.matricula:
                        turnos.append(turno)
                self.gestion_de_turnos.turnos = turnos
                self.gestion_de_turnos._guardar_turnos()
            print(f"Médico {medico.nombre} eliminado exitosamente.")
        else:
            print("Operación cancelada.")

    def guardar_cambios(self):
        self._guardar_medicos()
        print("Cambios guardados exitosamente.")
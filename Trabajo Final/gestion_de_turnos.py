from fecha import Fecha
from fecha_hora import FechaHora
from turno import Turno
from gestion_de_pacientes import GestionDePacientes
from gestion_de_medicos import GestionDeMedicos
import os
import pickle




class GestionDeTurnos:
    def __init__(self, archivo_turnos: str, gestion_pacientes: GestionDePacientes, gestion_medicos: GestionDeMedicos):
        self.archivo_turnos = archivo_turnos
        self.gestion_pacientes = gestion_pacientes
        self.gestion_medicos = gestion_medicos
        self.turnos: list[Turno] = self._cargar_turnos()

#--------------------------------FUNCIONES PRIVADAS--------------------------------#
    def _cargar_turnos(self) -> list[Turno]:
        if not os.path.exists(self.archivo_turnos):
            return []
        try:
            with open(self.archivo_turnos, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar_turnos(self):
        with open(self.archivo_turnos, "wb") as f:
            pickle.dump(self.turnos, f)

    def _verificar_medico_y_hora(self, medico, fecha_hora)-> bool:
        for turno in self.turnos:
            if (turno.medico.matricula == medico.matricula and
                turno.fecha_hora.anio == fecha_hora.anio and
                turno.fecha_hora.mes == fecha_hora.mes and
                turno.fecha_hora.dia == fecha_hora.dia and
                turno.fecha_hora.hora == fecha_hora.hora and
                turno.fecha_hora.minuto == fecha_hora.minuto):
                print(f"El médico {medico.nombre} ya tiene un turno agendado para esa fecha y hora.")
                return False
        return True

    def _verificar_paciente_y_hora(self, paciente, fecha_hora) -> bool:
        for turno in self.turnos:
            if (turno.paciente.DNI == paciente.DNI and
                turno.fecha_hora.anio == fecha_hora.anio and
                turno.fecha_hora.mes == fecha_hora.mes and
                turno.fecha_hora.dia == fecha_hora.dia and
                turno.fecha_hora.hora == fecha_hora.hora and
                turno.fecha_hora.minuto == fecha_hora.minuto):
                print(f"El paciente {paciente.nombre} ya tiene un turno agendado para esa fecha y hora.")
                return False
        return True

    def _turnos_en_fecha(self, fecha: Fecha) -> list[Turno]:
        turnos_en_fecha = []
        for turno in self.turnos:
            if (turno.fecha_hora.anio == fecha.anio and
                    turno.fecha_hora.mes == fecha.mes and
                    turno.fecha_hora.dia == fecha.dia):
                turnos_en_fecha.append(turno)
        return turnos_en_fecha

    def _pedir_fecha_hora(self, mensaje: str) -> FechaHora | None:
        while True:
            fecha_hora = input(mensaje).strip()
            try:
                return FechaHora(fecha_hora)
            except ValueError as e:
                print(f"Error: {e}")
                continuar = input("¿Desea intentar nuevamente? (s/n): ").strip().lower()
                if continuar != 's':
                    return None

    def _encontrar_turno_por_fecha_hora(self, fecha_hora) -> Turno | None:
        for turno in self.turnos:
            if (turno.fecha_hora.anio == fecha_hora.anio and
                turno.fecha_hora.mes == fecha_hora.mes and
                turno.fecha_hora.dia == fecha_hora.dia and
                turno.fecha_hora.hora == fecha_hora.hora and
                turno.fecha_hora.minuto == fecha_hora.minuto):
                return turno
        print(f"No se encontró un turno para la fecha y hora {fecha_hora}.")
        return None

#--------------------------------FUNCIONES PÚBLICAS--------------------------------#
    def listar_turnos(self):
        if not self.turnos:
            print("No hay turnos registrados.")
            return
        print("Lista de Turnos:")
        for turno in self.turnos:
            print(turno)

    def agregar_turno(self):
        fecha_hora = self._pedir_fecha_hora("Ingrese la fecha y hora del turno (dd/mm/aaaa HH:MM): ")
        if not fecha_hora:
            return
        dni = self.gestion_pacientes._validar_dni("Ingrese el DNI del paciente: ")
        if not dni:
            return
        paciente = self.gestion_pacientes._encontrar_paciente_por_dni(dni)
        if not paciente:
            return
        matricula = self.gestion_medicos._validar_matricula("Ingrese la matrícula del médico: ")
        if not matricula:
            return
        medico = self.gestion_medicos._encontrar_medico_por_matricula(matricula)
        if not medico:
            return
        if not self._verificar_medico_y_hora(medico, fecha_hora):
            return
        if not self._verificar_paciente_y_hora(paciente, fecha_hora):
            return
        motivo = input("Ingrese el motivo del turno (o presione enter para 'Consulta general'): ").strip() or "Consulta general"
        nuevo_turno = Turno(fecha_hora, paciente, medico,  motivo)
        self.turnos.append(nuevo_turno)
        self._guardar_turnos()
        print(f"Turno agregado exitosamente:")
        print(nuevo_turno)

    def listar_paciente_medico(self):
        if not self.turnos:
            print("No hay turnos registrados.")
            return
        while True:
            op = input("¿Desea listar turnos por Paciente (P) o Médico (M), (s para salir)? (P/M): ").strip().upper()
            if op == 'P':
                dni = self.gestion_pacientes._validar_dni("Ingrese el DNI del paciente: ")
                if not dni:
                    return
                paciente = self.gestion_pacientes._encontrar_paciente_por_dni(dni)
                if not paciente:
                    return
                print(f"Turnos del paciente {paciente.nombre}:")
                for turno in self.turnos:
                    if turno.paciente.DNI == dni:
                        print(turno)
            elif op == 'M':
                matricula = self.gestion_medicos._validar_matricula("Ingrese la matrícula del médico: ")
                if not matricula:
                    return
                medico = self.gestion_medicos._encontrar_medico_por_matricula(matricula)
                if not medico:
                    return
                print(f"Turnos del médico {medico.nombre}:")
                for turno in self.turnos:
                    if turno.medico.matricula == matricula:
                        print(turno)
            elif op == 'S':
                print("Operación cancelada.")
                return
            else:
                print("Opción inválida. Debe ser 'P' o 'M' o 'S'.")
                return

    def buscar_por_fecha(self):
        fecha_str = input("Ingrese la fecha del turno (dd/mm/aaaa): ").strip()
        try:
            fecha = Fecha(fecha_str)
        except ValueError as e:
            print(f"Error al crear la fecha: {e}")
            return
        turnos_en_fecha = self._turnos_en_fecha(fecha)
        if not turnos_en_fecha:
            print(f"No hay turnos registrados para la fecha {fecha}.")
            return
        print(f"Turnos registrados para la fecha {fecha}:")
        for turno in turnos_en_fecha:
            print(turno)

    def eliminar_turno(self):
        fecha_hora = self._pedir_fecha_hora("Ingrese la fecha y hora del turno a eliminar (dd/mm/aaaa HH:MM): ")
        turno_a_eliminar = self._encontrar_turno_por_fecha_hora(fecha_hora)
        if not turno_a_eliminar:
            return
        confirmacion = input(f"¿Está seguro de que desea eliminar el turno {turno_a_eliminar}? (s/n): ").strip().lower()
        if confirmacion == 's':
            self.turnos.remove(turno_a_eliminar)
            self._guardar_turnos()
            print(f"Turno {turno_a_eliminar} eliminado exitosamente.")
        else:
            print("Operación cancelada.")

    def guardar_cambios(self):
        self._guardar_turnos()
        print("Cambios guardados exitosamente.")
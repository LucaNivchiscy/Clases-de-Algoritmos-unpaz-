from fecha_hora import FechaHora
from paciente import Paciente
from medico import Medico


class Turno:
    def __init__(self, fecha_hora: FechaHora, paciente: Paciente, medico: Medico, motivo: str = "Consulta general"):
        if not isinstance(fecha_hora, FechaHora):
            raise TypeError("fecha_hora debe ser una instancia de la clase FechaHora.")
        if not isinstance(paciente, Paciente):
            raise TypeError("paciente debe ser una instancia de la clase Paciente.")
        if not isinstance(medico, Medico):
            raise TypeError("medico debe ser una instancia de la clase Medico.")
        self.fecha_hora = fecha_hora
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo


    def __str__(self):
        return (f"--- DETALLE DEL TURNO ---\n"
                f"Fecha y Hora: {self.fecha_hora}\n"
                f"  - Paciente: {self.paciente.nombre}\n"
                f"  - Médico: {self.medico.nombre}\n"
                f"  - Especialidad: {self.medico.especialidad}\n"
                f"  - Motivo: {self.motivo}\n"
                f"-------------------------")
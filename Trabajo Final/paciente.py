from fecha import Fecha


class Paciente:
    def __init__(self, DNI: str, nombre: str,fecha_nacimiento: Fecha ,obra_social: str="No Tiene obra social"):
        if not DNI.isdigit() or len(DNI) < 7:
            raise ValueError("El DNI debe ser numérico y tener al menos 7 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError("La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.DNI = DNI
        self.nombre = nombre
        self.obra_social = obra_social
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return (f"--- DATOS DEL PACIENTE ---\n"
                f"  - Nombre: {self.nombre}\n"
                f"  - DNI: {self.DNI}\n"
                f"  - Obra Social: {self.obra_social}\n"
                f"  - Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"--------------------------")
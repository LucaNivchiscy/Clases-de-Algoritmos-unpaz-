from fecha import Fecha

class Cliente:
    def __init__(self, dni: str, nombre: str, fecha_nacimiento: Fecha):
        if not dni.isdigit() or len(dni) < 7:
            raise ValueError(
                "El DNI debe ser numérico y tener al menos 7 dígitos.")
        if not isinstance(fecha_nacimiento, Fecha):
            raise TypeError(
                "La fecha de nacimiento debe ser una instancia de la clase Fecha.")
        self.dni = dni
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"Cliente {self.nombre} - DNI: {self.dni} - Nacimiento: {self.fecha_nacimiento}"

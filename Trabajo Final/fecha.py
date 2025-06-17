
from datetime import datetime


class Fecha:
    def __init__(self, fecha_str: str, horario_str: str = None):
        self.dt_objeto = None
        formato_fecha = "%d/%m/%Y"
        formato_fecha_hora = "%d/%m/%Y %H:%M"
        if horario_str:
            fecha_hora = f"{fecha_str} {horario_str}"
            try:
                fecha_dt = datetime.strptime(fecha_hora, formato_fecha_hora)
            except ValueError:
                raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")

            if fecha_dt < datetime.now():
                raise ValueError("La fecha no puede ser anterior a la fecha actual.")
        else:
            try:
                fecha_dt = datetime.strptime(fecha_str, formato_fecha)
            except ValueError:
                raise ValueError("Formato de fecha no válido. Debe ser dd/mm/aaaa")

        self.dt_objeto = fecha_dt
        self.dia = self.dt_objeto.day
        self.mes = self.dt_objeto.month
        self.anio = self.dt_objeto.year
        self.hora = self.dt_objeto.hour if horario_str else None
        self.minuto = self.dt_objeto.minute if horario_str else None

    def __str__(self):
        if self.hora is not None and self.minuto is not None:
            return self.dt_objeto.strftime("%d/%m/%Y %H:%M")
        else:
            return self.dt_objeto.strftime("%d/%m/%Y")
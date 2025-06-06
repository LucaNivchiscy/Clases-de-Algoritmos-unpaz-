from datetime import datetime
import re


class FechaHora:
    def __init__(self, fecha_hora_str: str = None):
        if not fecha_hora_str:
            ahora = datetime.now()
            self.dia = ahora.day
            self.mes = ahora.month
            self.anio = ahora.year
            self.hora = ahora.hour
            self.minuto = ahora.minute
        else:
            if not self.es_fecha_hora_valida(fecha_hora_str):
                raise ValueError('Formato no válido. Debe ser "dd/mm/aaaa HH:MM"')
            fecha_str, hora_str = fecha_hora_str.strip().split()
            self.dia, self.mes, self.anio = map(int, fecha_str.split('/'))
            self.hora, self.minuto = map(int, hora_str.split(':'))

            try:
                dt_ingresado = datetime.strptime(fecha_hora_str, "%d/%m/%Y %H:%M")
            except ValueError:
                raise ValueError("Fecha y hora no válidas. Deben ser dd/mm/aaaa HH:MM")
            if dt_ingresado < datetime.now():
                raise ValueError("La fecha y hora no pueden ser anteriores a la fecha y hora actual.")


    def es_fecha_hora_valida(self, fecha_hora: str) -> bool:
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01]\d|2[0-3]):([0-5]\d)$'
        return re.match(patron, fecha_hora) is not None

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}"
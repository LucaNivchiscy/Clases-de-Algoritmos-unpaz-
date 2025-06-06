#class FechaHora:
#     def __init__(self, fecha_str: str, horario_str: str = None):
#         self.dt_objeto = None
#         formato_fecha = "%d/%m/%Y"
#         formato_fecha_hora = "%d/%m/%Y %H:%M"
#         if horario_str:
#             fecha_hora = f"{fecha_str} {horario_str}"
#             try:
#                 fecha_dt = datetime.strptime(fecha_hora, formato_fecha_hora)
#             except ValueError:
#                 raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")
#             if fecha_dt < datetime.now():
#                 raise ValueError("La fecha y hora no pueden ser anteriores a la fecha y hora actual.")
#
#         else:
#             try:
#                 fecha_dt = datetime.strptime(fecha_str, formato_fecha)
#             except ValueError:
#                 raise ValueError("Formato de fecha no válido. Debe ser dd/mm/aaaa")
#
#         self.dt_objeto = fecha_dt
#         self.dia = self.dt_objeto.day
#         self.mes = self.dt_objeto.month
#         self.anio = self.dt_objeto.year
#         self.hora = self.dt_objeto.hour if horario_str else None
#         self.minuto = self.dt_objeto.minute if horario_str else None
#
#     def __str__(self):
#         if self.hora is not None and self.minuto is not None:
#             return self.dt_objeto.strftime("%d/%m/%Y %H:%M")
#         else:
#             return self.dt_objeto.strftime("%d/%m/%Y")
# class Fecha:
#     def __init__(self, fecha_str: str, horario_str: str = None):
#         if horario_str:
#             fecha_hora = f"{fecha_str} {horario_str}"
#             if not self.es_fecha_hora_valida(fecha_hora):
#                 raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")
#             partes_hora = horario_str.split(":")
#             self.hora = int(partes_hora[0])
#             self.minuto = int(partes_hora[1])
#         else:
#             if not self.es_fecha_valida(fecha_str):
#                 raise ValueError("Formato de fecha no válido. Debe ser dd/mm/aaaa")
#             self.hora = None
#             self.minuto = None
#
#         partes_fecha = fecha_str.split("/")
#         self.dia = int(partes_fecha[0])
#         self.mes = int(partes_fecha[1])
#         self.anio = int(partes_fecha[2])
#
#     def es_fecha_valida(self, fecha: str) -> bool:
#         patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
#         return re.match(patron, fecha) is not None
#
#     def es_fecha_hora_valida(self, fecha_hora: str) -> bool:
#         patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01][0-9]|2[0-3]):([0-5][0-9])$'
#         return re.match(patron, fecha_hora) is not None
#
#     def __str__(self):
#         if self.hora is not None and self.minuto is not None:
#             return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}"
#         else:
#             return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"
from cliente import Cliente
from producto import Product
from fecha_hora import FechaHora

class Compra:
    def __init__(self, cliente: Cliente, productos: list[Product], fecha_hora: FechaHora = FechaHora()):
        self.cliente = cliente
        self.productos = productos
        self.fecha_hora = fecha_hora
        self.importe_total = self._calcular_importe_total()

    def _calcular_importe_total(self):
        importe_total = 0
        for producto in self.productos:
            importe_total += producto.precio
        return importe_total


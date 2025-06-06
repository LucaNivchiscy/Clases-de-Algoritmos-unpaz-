import pickle
import os

from gestor_clientes import GestorDeClientes
from gestor_productos import GestorDeProductos
from cliente import Cliente
from producto import Product
from compra import Compra

class GestorDeCompras:

    def __init__(self, archivo, gestor_de_clientes: GestorDeClientes, gestor_de_productos: GestorDeProductos):
        self.archivo = archivo
        self.lista_de_compras: list[Compra] = self._cargar()
        self.gestor_clientes = gestor_de_clientes
        self.gestor_productos = gestor_de_productos

    def _cargar(self):
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar(self):
        with open(self.archivo, "wb") as f:
            pickle.dump(self.lista_de_compras, f)

    def listar_compras(self):
        if not self.lista_de_compras:
            print("No hay compras registradas")
        for compra in self.lista_de_compras:
            print(compra)

    def crear_compra(self):
        dni_cliente = self.gestor_clientes._input_dni("Ingrese el DNI del cliente: ")
        cliente_encontrado: Cliente = self.gestor_clientes._buscar_por_dni(dni_cliente)
        if not cliente_encontrado:
            print(f"No existe el cliente con DNI {dni_cliente}")
            return
        productos: list[Product] = []
        while True:
            codigo_producto = self.gestor_productos._input_codigo("Ingrese el código del producto a agregar a la compra: ")
            producto_encontrado = self.gestor_productos._buscar_por_codigo(codigo_producto)
            if not producto_encontrado:
                print(f"El código {codigo_producto} no corresponde con un producto válido")
            else:
                productos.append(producto_encontrado)
                desea_cargar_mas_productos = input("¿Desea seguir cargando productos? (s/n): ").lower()
                if desea_cargar_mas_productos not in ("s", "si"):
                    break
        nueva_compra = Compra(cliente_encontrado, productos)
        self.lista_de_compras.append(nueva_compra)
        self._guardar()

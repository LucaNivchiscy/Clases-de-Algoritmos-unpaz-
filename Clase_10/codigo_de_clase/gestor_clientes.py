import os
import pickle
from cliente import Cliente
from fecha import Fecha

class GestorDeClientes:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.clientes = self._cargar()

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
            pickle.dump(self.clientes, f)

    def _buscar_por_dni(self, dni: str) -> Cliente:
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None

    def _input_dni(self, mensaje="Ingrese el DNI: "):
        dni = input(mensaje).strip()
        if not dni.isdigit() or len(dni) < 7:
            print("DNI inválido. Debe ser numérico y tener al menos 7 dígitos.")
            return None
        return dni

    def _pedir_fecha_de_nacimiento_valida(self):
        while True:
            fecha_str = input("Fecha de nacimiento (dd/mm/aaaa): ").strip()
            try:
                return Fecha(fecha_str)
            except ValueError:
                print("Error en el formato. Intente nuevamente.")

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes para mostrar.")
            return
        for c in self.clientes:
            print(c)

    def buscar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if cliente:
            print(cliente)
        else:
            print("Cliente no encontrado.")

    def agregar_cliente(self):
        dni = self._input_dni("Nuevo DNI: ")
        if dni is None:
            return
        if self._buscar_por_dni(dni):
            print("Ya existe un cliente con ese DNI.")
            return
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        fecha_nacimiento = self._pedir_fecha_de_nacimiento_valida()
        cliente = Cliente(dni, nombre, fecha_nacimiento)
        self.clientes.append(cliente)
        self._guardar()
        print("Cliente agregado.")

    def modificar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre ({cliente.nombre}): ").strip()
        cliente.nombre = nuevo_nombre
        cliente.fecha_nacimiento = self._pedir_fecha_de_nacimiento_valida()
        self._guardar()
        print("Cliente modificado.")

    def eliminar_cliente(self):
        dni = self._input_dni()
        if dni is None:
            return
        cliente = self._buscar_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        confirmar = input(
            f"¿Seguro que desea eliminar al cliente '{cliente.nombre}'? (s/n): ").lower()
        if confirmar == "s":
            self.clientes.remove(cliente)
            self._guardar()
            print("Cliente eliminado.")

    def guardar(self):
        self._guardar()
        print("Cambios guardados.")
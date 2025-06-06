import os
import pickle
from producto import Product

class GestorDeProductos:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.productos: list[Product] = self._cargar()

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
            pickle.dump(self.productos, f)

    def _buscar_por_codigo(self, codigo: int) -> Product:
        for producto in self.productos:
            if producto.codigo == codigo:
                return  producto
        return None

    def _input_codigo(self, mensaje="Ingrese el código del producto: "):
        try:
            return int(input(mensaje))
        except ValueError:
            print("Código inválido.")
            return None

    def listar_productos(self):
        if not self.productos:
            print("No hay productos para mostrar.")
            return
        for p in self.productos:
            print(p)

    def buscar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    def agregar_producto(self):
        codigo = self._input_codigo("Nuevo código: ")
        if codigo is None:
            return
        if self._buscar_por_codigo(codigo):
            print("Ya existe un producto con ese código.")
            return
        nombre = input("Nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                print("El precio no puede ser negativo.")
                return
            producto = Product(codigo, nombre, precio)
            self.productos.append(producto)
            self._guardar()
            print("Producto agregado.")
        except ValueError:
            print("Precio inválido.")

    def modificar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        nuevo_nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip()
        if nuevo_nombre:
            producto.nombre = nuevo_nombre
        nuevo_precio = input(f"Nuevo precio ({producto.precio}): ").strip()
        if nuevo_precio:
            try:
                precio = float(nuevo_precio)
                if precio < 0:
                    print("El precio no puede ser negativo.")
                    return
                producto.precio = precio
            except ValueError:
                print("Precio inválido.")
                return
        self._guardar()
        print("Producto modificado.")

    def eliminar_producto(self):
        codigo = self._input_codigo()
        if codigo is None:
            return
        producto = self._buscar_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        confirmar = input(
            f"¿Seguro que desea eliminar '{producto.nombre}'? (s/n): ").lower()
        if confirmar == "s":
            self.productos.remove(producto)
            self._guardar()
            print("Producto eliminado.")

    def guardar(self):
        self._guardar()
        print("Cambios guardados.")
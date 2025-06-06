import pickle
import os
from datetime import datetime
import re


# ---------------------------------------Clase Fecha--------------------------
class Fecha:
    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            if not self.es_fecha_valida(fecha_str):
                raise ValueError(
                    'Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

# ---------------------------------------Clase FechaHora--------------------------
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
                raise ValueError("Formato de fecha y hora no válido. Debe ser dd/mm/aaaa hh:mm")

            fecha_str, hora_str = fecha_hora_str.strip().split(" ")
            partes_fecha = fecha_str.split("/")
            partes_hora = hora_str.split(":")

            self.dia = int(partes_fecha[0])
            self.mes = int(partes_fecha[1])
            self.anio = int(partes_fecha[2])
            self.hora = int(partes_hora[0])
            self.minuto = int(partes_hora[1])

    def es_fecha_hora_valida(self, fecha_hora: str) -> bool:
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01][0-9]|2[0-3]):([0-5][0-9])$'
        return re.match(patron, fecha_hora) is not None

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio} {self.hora:02d}:{self.minuto:02d}"


#-------------------------------------Clase Producto--------------------------
class Product:
    def __init__(self, cod: int, name: str, price: float):
        if price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.codigo: int = cod
        self.nombre: str = name
        self.precio: float = price

    def __str__(self):
        return f"Producto ({self.codigo}): {self.nombre} - Precio: ${self.precio:.2f}"

    def aplicar_descuento(self, porcentaje: float) -> float:
        if not isinstance(porcentaje, (int, float)):
            raise TypeError("El porcentaje debe ser un número.")
        if not (1 <= porcentaje <= 100):
            raise ValueError("El porcentaje debe estar entre 1 y 100.")
        descuento = self.precio * (porcentaje / 100)
        return round(self.precio - descuento, 2)



#-------------------------------------Clase Cliente--------------------------

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


#-------------------------------------Clase Compra--------------------------
class Compra:
    def __init__(self, cliente: Cliente, productos: list[Product], fecha_hora: FechaHora = None):
        self.cliente = cliente
        self.productos = productos
        self.fecha_hora = fecha_hora if fecha_hora is not None else FechaHora()
        self.importe_total = self._calcular_importe_total()

    def _calcular_importe_total(self):
        importe_total = 0
        for producto in self.productos:
            importe_total += producto.precio
        return importe_total

    def __str__(self):
        return f"Compra de {self.cliente.nombre} ({self.cliente.dni}) - Fecha: {self.fecha_hora} - Total: ${self.importe_total:.2f}\n" + \
                "\n".join([f"  - {producto.nombre} (${producto.precio:.2f})" for producto in self.productos])

#-------------------------------------Gestor de Productos--------------------------

class GestorProductos:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.productos: list[Product] = self._cargar()

#--Metodos Privados--
    def _guardar(self):
        """Guarda la lista de productos en el archivo."""
        with open(self.archivo, "wb") as f:
            pickle.dump(self.productos, f)

    def _cargar(self):
        """Carga los productos desde el archivo.
        En caso de no encontrar el archivo o si está vacío, retorna una lista vacía."""
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _validar_codigo(self, mensaje="Ingrese el código del producto: "):
        """Valida que el código ingresado sea un número entero."""
        try:
            codigo = int(input(mensaje))
            return codigo
        except ValueError:
            print("Código inválido.")
            return None

    def _buscar_producto_por_codigo(self, codigo):
        """Busca un producto por el codigo que recibe."""
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def _modificar_todo(self, producto):
        """Permite modificar tanto el nombre como el precio del producto."""
        nuevo_nombre = input(f"Nuevo nombre (actual: {producto.nombre}): ")
        if not nuevo_nombre:
            print("El nombre no puede estar vacío.")
            return
        producto.nombre = nuevo_nombre
        try:
            nuevo_precio = float(input(f"Nuevo precio (actual: ${producto.precio:.2f}): "))
            if nuevo_precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            producto.precio = nuevo_precio
        except ValueError as e:
            print(e)
            return
        self._guardar()
        print("Producto modificado.")

#--Metodos Públicos--
    def listar_productos(self):
        if not self.productos:
            print("No hay productos para mostrar.")
            return
        for p in self.productos:
            print(p)

    def buscar_producto(self):
        codigo = self._validar_codigo()
        if not codigo:
            return
        producto = self._buscar_producto_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        print(producto)

    def agregar_producto(self):
        codigo = self._validar_codigo("Nuevo código: ")
        if not codigo:
            return
        if self._buscar_producto_por_codigo(codigo):
            print("Ya existe un producto con ese código.")
            return
        nombre = input("Nombre: ")
        if not nombre:
            print("El nombre no puede estar vacio.")
            return
        try:
            precio = float(input("Precio: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
        except ValueError as e:
            print(e)
            return
        producto = Product(codigo, nombre, precio)
        self.productos.append(producto)
        self._guardar()
        print("Producto agregado.")

    def modificar_producto(self):
        codigo = self._validar_codigo()
        if not codigo:
            return
        producto = self._buscar_producto_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        while True:
            op = input("¿Qué desea modificar? (1: Nombre, 2: Precio, 3: Todo, 0: Salir): ")
            if op == '1':
                nuevo_nombre = input(f"Nuevo nombre (actual: {producto.nombre}): ")
                if not nuevo_nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                if nuevo_nombre:
                    producto.nombre = nuevo_nombre
                    self._guardar()
                    print("Nombre modificado.")
                    return
            elif op == '2':
                try:
                    nuevo_precio = float(input(f"Nuevo precio (actual: ${producto.precio:.2f}): "))
                    if nuevo_precio < 0:
                        raise ValueError("El precio no puede ser negativo.")
                    producto.precio = nuevo_precio
                    self._guardar()
                    print("Precio modificado.")
                    return
                except ValueError as e:
                    print(e)
                    continue
            elif op == '3':
                self._modificar_todo(producto)
                break
            elif op == '0':
                print("Modificación cancelada.")
                return
            else:
                print("Opción inválida. Intente de nuevo.")

    def eliminar_producto(self):
        codigo = self._validar_codigo()
        if not codigo:
            return
        producto = self._buscar_producto_por_codigo(codigo)
        if not producto:
            print("Producto no encontrado.")
            return
        self.productos.remove(producto)
        self._guardar()
        print("Producto eliminado.")

    def guardar(self):
        """Guarda los cambios realizados en la lista de productos."""
        self._guardar()
        print("Cambios guardados.")


class GestorClientes:
    def __init__(self, archivo: str):
        self.archivo = archivo
        self.clientes: list[Cliente] = self._cargar()
#--Metodos Privados--
    def _cargar(self):
        """Carga los clientes desde el archivo.
        En caso de no encontrar el archivo o si está vacío, retorna una lista vacía."""
        if not os.path.exists(self.archivo):
            return []
        try:
            with open(self.archivo, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def _guardar(self):
        """Guarda la lista de clientes en el archivo."""
        with open(self.archivo, "wb") as f:
            pickle.dump(self.clientes, f)

    def _validar_dni(self, mensaje="Ingrese el DNI del cliente: "):
        """valida que el DNI ingresado sea un número entero de al menos 7 dígitos."""
        dni = input(mensaje).strip()
        if not dni.isdigit() or len(dni) < 7:
            print("El DNI debe ser numérico y tener al menos 7 dígitos.")
            return None
        return dni

    def _buscar_cliente_por_dni(self, dni):
        """Busca un cliente por el DNI que recibe."""
        for cliente in self.clientes:
            if cliente.dni == dni:
                return cliente
        return None
#--Metodos Públicos--

    def listar_clientes(self):
        if not self.clientes:
            print("No hay clientes para mostrar.")
            return
        for c in self.clientes:
            print(c)

    def buscar_cliente(self):
        dni = self._validar_dni()
        if not dni:
            return
        cliente = self._buscar_cliente_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        print(cliente)

    def agregar_cliente(self):
        nuevo_dni = self._validar_dni("Nuevo DNI: ")
        if not nuevo_dni:
            return
        if self._buscar_cliente_por_dni(nuevo_dni):
            print("Ya existe un cliente con ese DNI.")
            return
        nombre = input("Nombre: ")
        if not nombre:
            print("El nombre no puede estar vacío.")
            return
        fecha_de_nacimiento = input("Fecha de nacimiento (dd/mm/aaaa): ")
        cliente = Cliente(nuevo_dni, nombre, Fecha(fecha_de_nacimiento))
        self.clientes.append(cliente)
        self._guardar()
        print("Cliente agregado.")

    def modificar_cliente(self):
        dni = self._validar_dni("ingrese el DNI del cliente a modificar: ")
        if not dni:
            return
        cliente = self._buscar_cliente_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        while True:
            op = input("¿Qué desea modificar? (1: Nombre, 2: Fecha de nacimiento, 0: Salir): ")
            if op == '1':
                nuevo_nombre = input(f"Nuevo nombre (actual: {cliente.nombre}): ")
                if not nuevo_nombre:
                    print("El nombre no puede estar vacío.")
                    continue
                cliente.nombre = nuevo_nombre
                self._guardar()
                print("Nombre modificado.")
                return
            elif op == '2':
                nueva_fecha = input(f"Nueva fecha de nacimiento (actual: {cliente.fecha_nacimiento}): ")
                try:
                    cliente.fecha_nacimiento = Fecha(nueva_fecha)
                    self._guardar()
                    print("Fecha de nacimiento modificada.")
                    return
                except ValueError as e:
                    print(e)
                    continue
            elif op == '0':
                print("Modificación cancelada.")
                return
            else:
                print("Opción inválida. Intente de nuevo.")

    def eliminar_cliente(self):
        dni = self._validar_dni("Ingrese el DNI del cliente a eliminar: ")
        if not dni:
            return
        cliente = self._buscar_cliente_por_dni(dni)
        if not cliente:
            print("Cliente no encontrado.")
            return
        self.clientes.remove(cliente)
        self._guardar()
        print("Cliente eliminado.")

    def guardar(self):
        """Guarda los cambios realizados en la lista de clientes."""
        self._guardar()
        print("Cambios guardados.")

class GestorCompras:
    def __init__(self, archivo: str, gestor_productos: GestorProductos, gestor_clientes: GestorClientes):
        self.archivo = archivo
        self.compras: list[Compra] = self._cargar()
        self.gestor_productos = gestor_productos
        self.gestor_clientes = gestor_clientes

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
            pickle.dump(self.compras, f)

    def listar_compras(self):
        if not self.compras:
            print("no hay compras registradas.")
            return
        for compra in self.compras:
            print(compra)

    def registrar_compra(self):
        dni_cliente = self.gestor_clientes._validar_dni("Ingrese el DNI del Cliente: ")
        if not dni_cliente:
            return
        cliente = self.gestor_clientes._buscar_cliente_por_dni(dni_cliente)
        if not cliente:
            print(f"No existe un cliente con DNI {dni_cliente}.")
            return
        productos = []
        while True:
            codigo_producto = self.gestor_productos._validar_codigo("Ingrese el código del producto a agregar a la compra (o 0 para finalizar): ")
            if not codigo_producto:
                continue
            if codigo_producto == 0:
                break
            producto = self.gestor_productos._buscar_producto_por_codigo(codigo_producto)
            if not producto:
                print(f"El código {codigo_producto} no corresponde con un producto válido.")
                opcion = input("¿Desea intentar con otro código? (s/n): ").lower()
                if opcion not in ("s", "si"):
                    break
            else:
                productos.append(producto)
                desea_cargar_mas_productos = input("¿Desea seguir cargando productos? (s/n): ").lower()
                if desea_cargar_mas_productos not in ("s", "si"):
                    break
        nueva_compra = Compra(cliente, productos)
        self.compras.append(nueva_compra)
        print("Compra registrada exitosamente.")
        self._guardar()


    def buscar_compra(self):
        dni_cliente = self.gestor_clientes._validar_dni("Ingrese el DNI del Cliente: ")
        if not dni_cliente:
            return
        cliente = self.gestor_clientes._buscar_cliente_por_dni(dni_cliente)
        if not cliente:
            print(f"No existe un cliente con DNI {dni_cliente}.")
            return
        compras_cliente = self._compras_por_cliente(dni_cliente)
        if not compras_cliente:
            print(f"No hay compras registradas para el cliente con DNI {dni_cliente}.")
            return
        print(f"Compras del cliente {cliente.nombre} ({cliente.dni}):")
        for compra in compras_cliente:
            print(compra)

    def _compras_por_cliente(self, dni_cliente):
        compras_encontradas = []
        for compra in self.compras:
            if compra.cliente.dni == dni_cliente:
                compras_encontradas.append(compra)
        return compras_encontradas


    def eliminar_compra(self):
        dni_cliente = self.gestor_clientes._validar_dni("Ingrese el DNI del Cliente: ")
        if not dni_cliente:
            return
        cliente = self.gestor_clientes._buscar_cliente_por_dni(dni_cliente)
        if not cliente:
            print(f"No existe un cliente con DNI {dni_cliente}.")
            return
        compras_cliente = self._compras_por_cliente(dni_cliente)
        if not compras_cliente:
            print(f"No hay compras registradas para el cliente con DNI {dni_cliente}.")
            return
        while True:
            op = input("¿Desea eliminar la compra? (s/n): ").lower()
            if op in ('s', 'si'):
                self.compras.remove(compras_cliente)
                print("Compra eliminada exitosamente.")
                self._guardar()
                return
            elif op in ('n', 'no'):
                print("Eliminación cancelada.")
                return
            else:
                print("Opción inválida. Intente de nuevo.")

    def guardar(self):
        self._guardar()
        print("Cambios guardados.")
#-------------------------------------Menu Principal--------------------------


class Menu:
    def __init__(self, opciones: list[str]):
        self.opciones = opciones

    def mostrar(self):
        print("\n--- Menú ---")
        for i, texto in enumerate(self.opciones, 1):
            print(f"{i}. {texto}")

    def pedir_opcion(self) -> int:
        while True:
            try:
                seleccion = int(input("Seleccione una opción: "))
                if 1 <= seleccion <= len(self.opciones):
                    return seleccion
                else:
                    print("Opción fuera de rango.")
            except ValueError:
                print("Debe ingresar un número entero válido.")

def menu_clientes(gestor_clientes: GestorClientes):
    menu = Menu([
        "Listar clientes",
        "Buscar cliente por DNI",
        "Agregar cliente",
        "Modificar cliente",
        "Eliminar cliente",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestor_clientes.listar_clientes()
        elif opcion == 2:
            gestor_clientes.buscar_cliente()
        elif opcion == 3:
            gestor_clientes.agregar_cliente()
        elif opcion == 4:
            gestor_clientes.modificar_cliente()
        elif opcion == 5:
            gestor_clientes.eliminar_cliente()
        elif opcion == 6:
            gestor_clientes.guardar()
        elif opcion == 7:
            break


def menu_productos(gestor_productos: GestorProductos):
    menu = Menu([
        "Listar productos",
        "Buscar producto por código",
        "Agregar producto",
        "Modificar producto",
        "Eliminar producto",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestor_productos.listar_productos()
        elif opcion == 2:
            gestor_productos.buscar_producto()
        elif opcion == 3:
            gestor_productos.agregar_producto()
        elif opcion == 4:
            gestor_productos.modificar_producto()
        elif opcion == 5:
            gestor_productos.eliminar_producto()
        elif opcion == 6:
            gestor_productos.guardar()
        elif opcion == 7:
            break

def menu_compras(gestor: GestorCompras):
    menu = Menu([
        "Listar compras",
        "Registrar nueva compra",
        "Buscar compra por DNI",
        "Eliminar compra",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestor.listar_compras()
        elif opcion == 2:
            gestor.registrar_compra()
        elif opcion == 3:
            gestor.buscar_compra()
        elif opcion == 4:
            gestor.eliminar_compra()
        elif opcion == 5:
            gestor.guardar()
        elif opcion == 6:
            break

def main():
    gestor_productos: GestorProductos = GestorProductos("Datos/productos.bin")
    gestor_clientes: GestorClientes = GestorClientes("Datos/clientes.bin")
    gestor_compras: GestorCompras = GestorCompras("Datos/compras.bin", gestor_productos, gestor_clientes)

    menu_principal = Menu([
        "Gestión de Productos",
        "Gestión de Clientes",
        "Gestión de Compras",
        "Salir"
    ])

    while True:
        menu_principal.mostrar()
        opcion = menu_principal.pedir_opcion()
        if opcion == 1:
            menu_productos(gestor_productos)
        elif opcion == 2:
            menu_clientes(gestor_clientes)
        elif opcion == 3:
            menu_compras(gestor_compras)
        elif opcion == 4:
            print("Saliendo del programa...")
            break


main()












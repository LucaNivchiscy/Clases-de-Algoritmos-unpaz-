"""Una empresa comercializa 10 artículos en 3 sucursales.
Se debe realizar un programa que permita gestionar el inventario y el stock por sucursal para dicha empresa.
Para ello se solicita que el programa posea un menú con las siguientes opciones:

A) Gestión de sucursales. CRUD considerando que toda sucursal tiene un código único (entero), un nombre y una dirección.
B) Gestión de artículos. CRUD considerando que todo artículo tiene un código único (entero), un nombre, una categoría y una descripción.
C) Carga de stock: se registrará el ingreso en depósito de la cantidad de un determinado artículo en una sucursal.
D) Venta de artículos: se registran las ventas realizadas informando sucursal, artículo y cantidad vendida.
    Se debe verificar que la cantidad vendida no exceda el stock de ese producto en esa sucursal,
    informando si la venta no se puede realizar por este motivo
E) Existencia de mercaderías: listar por pantalla cantidad existentes de mercaderías por sucursal
F) Salir del programa"""



class Articulo:
    def __init__(self, codigo: int, nombre: str, categoria: str, descripcion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.descripcion = descripcion
        self.stock_art = 0

    def __str__(self):
        return f"ID: {self.codigo}, Nombre: {self.nombre}, Categoria: {self.categoria}, Descripcion: {self.descripcion}, Stock: {self.stock_art}"


class Sucursal:
    def __init__(self, codigo, nombre: str, direccion: str):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.stock_lista = []

    def __str__(self):
        return f"ID: {self.codigo}, Nombre: {self.nombre}, Direccion: {self.direccion}"



class GestionArticulo:
    def __init__(self):
        self.articulos = []

    def crear_articulo(self):
        codigo = int(input("Ingrese el código del artículo: "))
        if codigo in [a.codigo for a in self.articulos]:
            print("El código del artículo ya existe.")
            return
        nombre = input("Ingrese el nombre del artículo: ")
        categoria = input("Ingrese la categoría del artículo: ")
        descripcion = input("Ingrese la descripción del artículo: ")

        nuevo_articulo = Articulo(codigo, nombre, categoria, descripcion)
        self.articulos.append(nuevo_articulo)

    def mostrar_articulos(self):
        if not self.articulos:
            print("No hay artículos registrados.")
            return
        for a in self.articulos:
            print(a)

    def actualizar_articulo(self, codigo):
        articulo = self.validar_articulo(codigo)
        if not articulo:
            print("Artículo no encontrado.")
            return
        nombre = input("Ingrese el nuevo nombre del artículo: ")
        categoria = input("Ingrese la nueva categoría del artículo: ")
        descripcion = input("Ingrese la nueva descripción del artículo: ")
        articulo.nombre = nombre
        articulo.categoria = categoria
        articulo.descripcion = descripcion
        print(f"Artículo actualizado: {articulo}")

    def eliminar_articulo(self, codigo):
        articulo = self.validar_articulo(codigo)
        if not articulo:
            print("Artículo no encontrado.")
            return
        self.articulos.remove(articulo)
        print(f"Artículo eliminado: {articulo}")


    def validar_articulo(self, codigo):
        for a in self.articulos:
            if a.codigo == codigo:
                return a
        return None


class GestionSucursal:
    def __init__(self,gestion_articulo: GestionArticulo):
        self.sucursales =[]
        self.gestion_articulo = gestion_articulo

    def crear_sucursal(self):
        codigo = int(input("Ingrese el código de la sucursal: "))
        if codigo in [s.codigo for s in self.sucursales]:
            print("El código de la sucursal ya existe.")
            return
        nombre = input("Ingrese el nombre de la sucursal: ")
        direccion = input("Ingrese la dirección de la sucursal: ")

        nueva_sucursal = Sucursal(codigo, nombre, direccion)
        self.sucursales.append(nueva_sucursal)
        print(f"Sucursal creada: {nueva_sucursal}")

    def ver_sucursales(self):
        if not self.sucursales:
            print("No hay sucursales registradas.")
            return
        for s in self.sucursales:
            print(s)

    def eliminar_sucursal(self, codigo):
        sucursal =  self.validar_sucursal(codigo)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        self.sucursales.remove(sucursal)
        print(f"Sucursal eliminada: {sucursal}")


    def actualizar_sucursal(self, codigo):
        sucursal = self.validar_sucursal(codigo)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        nombre = input("Ingrese el nuevo nombre de la sucursal: ")
        direccion = input("Ingrese la nueva dirección de la sucursal: ")
        sucursal.nombre = nombre
        sucursal.direccion = direccion
        print(f"Sucursal actualizada: {sucursal}")


    def ver_sucursal_codigo(self, codigo):
        sucursal = self.validar_sucursal(codigo)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        print(sucursal)



    def validar_sucursal(self, codigo):
        for s in self.sucursales:
            if s.codigo == codigo:
                return s
        return None


class GestionStock:
    def __init__(self, gestion_articulo: GestionArticulo, gestion_sucursal: GestionSucursal):
        self.gestion_articulo = gestion_articulo
        self.gestion_sucursal = gestion_sucursal


    def carga_stock(self):
        codigo_sucursal = int(input("Ingrese el código de la sucursal: "))
        sucursal = self.gestion_sucursal.validar_sucursal(codigo_sucursal)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        codigo_articulo = int(input("Ingrese el código del artículo: "))
        articulo = self.gestion_articulo.validar_articulo(codigo_articulo)
        if not articulo:
            print("Artículo no encontrado.")
            return
        cantidad = int(input("Ingrese la cantidad a cargar en stock: "))
        articulo.stock_art += cantidad
        sucursal.stock_lista.append(articulo)
        print(f"Stock actualizado para {articulo.nombre} en {sucursal.nombre}. Nuevo stock: {articulo.stock_art}")

    def venta_articulo(self):
        codigo_sucursal = int(input("Ingrese el código de la sucursal: "))
        sucursal = self.gestion_sucursal.validar_sucursal(codigo_sucursal)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        codigo_articulo = int(input("Ingrese el código del artículo: "))
        articulo = self.gestion_articulo.validar_articulo(codigo_articulo)
        if not articulo:
            print("Artículo no encontrado.")
            return
        cantidad = int(input("Ingrese la cantidad a vender: "))
        if cantidad > articulo.stock_art:
            print(f"No se puede realizar la venta. Stock insuficiente. Stock actual: {articulo.stock_art}")
            return
        articulo.stock_art -= cantidad
        print(f"Venta realizada. Nuevo stock de {articulo.nombre} en {sucursal.nombre}: {articulo.stock_art}")


    def existencias_sucursales(self):
        codigo =  int(input("Ingrese el código de la sucursal: "))
        sucursal =  self.gestion_sucursal.validar_sucursal(codigo)
        if not sucursal:
            print("Sucursal no encontrada.")
            return
        print(f"Existencias en {sucursal.nombre}:")
        for articulo in sucursal.stock_lista:
            if not articulo.stock_art:
                print(f"{articulo.nombre}: No hay stock")
                return
            print(f"{articulo.nombre}: {articulo.stock_art} unidades")


class Menu:
    def __init__(self):
        self.opciones_menu = [
            ["1. Crear Sucursal", "2. Ver Sucursales","3. Ver sucursal por codigo", "4. Actualizar Sucursal", "5. Eliminar Sucursal", "6. Salir"],
            ["1. Crear Articulo", "2. Ver Articulos", "3. Actualizar Articulo", "4. Eliminar Articulo", "5. Salir"],
            ["1. Gestor de sucursales","2. Gestor de Articulos","3. Cargar Stock", "4. Vender Articulo", "5. Existencias por Sucursal","6. Salir"],
        ]

    def mostrar_menu(self, opcion):
        print("Menu de Opciones:")
        for i in self.opciones_menu[opcion]:
            print(i)


    def opcion_selecionada(self):
        opcion = input("Seleccione una opción: ")
        return opcion


class Aplicacion:
    def __init__(self):
        self.gestion_articulo = GestionArticulo()
        self.gestion_sucursal = GestionSucursal(self.gestion_articulo)
        self.gestion_stock = GestionStock(self.gestion_articulo, self.gestion_sucursal)
        self.menu = Menu()

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu(2)
            opcion = self.menu.opcion_selecionada()
            if opcion == '1':
                while True:
                    self.menu.mostrar_menu(0)
                    opcion = self.menu.opcion_selecionada()
                    if opcion == '1':
                        self.gestion_sucursal.crear_sucursal()
                    elif opcion == '2':
                        self.gestion_sucursal.ver_sucursales()
                    elif opcion == '3':
                        self.gestion_sucursal.ver_sucursal_codigo(int(input("Ingrese el codigo de la sucursal: ")))
                    elif opcion == '4':
                        self.gestion_sucursal.actualizar_sucursal(int(input("Ingrese el codigo de la sucursal: ")))
                    elif opcion == '5':
                        self.gestion_sucursal.eliminar_sucursal(int(input("Ingrese el codigo de la sucursal: ")))
                    elif opcion == '6':
                        break
            elif opcion == '2':
                while True:
                    self.menu.mostrar_menu(1)
                    opcion = self.menu.opcion_selecionada()
                    if opcion == '1':
                        self.gestion_articulo.crear_articulo()
                    elif opcion == '2':
                        self.gestion_articulo.mostrar_articulos()
                    elif opcion == '3':
                        self.gestion_articulo.actualizar_articulo(int(input("Ingrese el codigo del articulo: ")))
                    elif opcion == '4':
                        self.gestion_articulo.eliminar_articulo(int(input("Ingrese el codigo del articulo: ")))
                    elif opcion == '5':
                        break
            elif opcion == '3':
                self.gestion_stock.carga_stock()
            elif opcion == '4':
                self.gestion_stock.venta_articulo()
            elif opcion == '5':
                self.gestion_stock.existencias_sucursales()
            elif opcion == '6':
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")





ejecutar = Aplicacion()
ejecutar.ejecutar()









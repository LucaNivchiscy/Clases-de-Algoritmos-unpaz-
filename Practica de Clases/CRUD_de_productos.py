"""📌 Consigna:
Crear una clase Producto con id, nombre, y precio. Luego, una clase Inventario que permita:

Crear/agregar productos.

Leer (listar todos los productos).

Actualizar precio por id.

Eliminar producto por id."""


class Producto:
    def __init__(self , id: int, nombre: str, precio: float):
        self.id = id
        self.nombre = nombre
        self.precio = precio


class Inventario:
    def __init__(self):
        self.productos: list[Producto] = []
    #menu
    def menu(self):
        print("Bienvenido al sistema de inventario")
        print("1. Crear producto")
        print("2. Listar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Salir")
    def menu2(self):
        print("Actualizar producto")
        print("1. Actualizar precio por id")
        print("2. Actualizar nombre por id")
        print("3. Volver al menu principal")

    #funcuiones de validacion (id, nombre y precio)
    def _crear_id(self):
        if not self.productos:  #si productos esta vacio, retorna 1
            return 1
        #max() devuelve el numero maximo de la lista, ej: max([1,2,3]) = 3
        return max(p.id for p in self.productos) + 1 #for p in self.productos, devuelve el id maximo de los productos y le suma 1

    def _validar_id(self):
        id = input("ingrese un id: ")
        if not id.isdigit():
            print("el id debe ser un numero")
            return False
        id_int = int(id)
        return id_int
    def _validar_nombre(self):
        nombre = input("ingrese un nombre: ").capitalize()
        if not nombre.isalpha():
            print("el nombre no puede contener numeros")
            return False
        return nombre
    def _validar_precio(self):
        precio = input("ingrese un precio: ")
        if not precio.isdigit():
            print("el precio debe ser un numero")
            return False
        precio_float = float(precio)
        return precio_float
    #funciones CRUD
    #crear producto
    def crear_producto(self):
        id = self._crear_id()
        nombre = self._validar_nombre()
        precio = self._validar_precio()
        if id == False or nombre == False or precio == False:
            print("error al crear el producto")
            return
        nuevo_producto = Producto(id, nombre, precio)
        self.productos.append(nuevo_producto)
        print(f"Producto {nombre} agregado con éxito.")

    #listar productos
    def listar_productos(self):
        if not self.productos:
            print("No hay productos en el inventario.")
            return False
        for producto in self.productos:
            print(f"ID: {producto.id}, Nombre: {producto.nombre}, Precio: {producto.precio} $")
            print("-"* 20)
        return True
    #actualizar prodcuto por Id
        #actualizar precio
    def actualizar_precio(self):
        validar = self.listar_productos()
        if not validar:
            return False
        id = self._validar_id()
        for producto in self.productos:
            if producto.id == id:
                nuevo_precio = self._validar_precio()
                if not nuevo_precio:
                    print("error al actualizar precio")
                    return False
                producto.precio = nuevo_precio
                print(f"Precio del producto {producto.nombre} actualizado a {nuevo_precio}.")
        print("el id no existe")
        return False
        #actualizar nombre
    def actualizar_nombre(self):
        validar = self.listar_productos()
        if not validar:
            return False
        id = self._validar_id()
        for producto in self.productos:
            if producto.id == id:
                nuevo_nombre = self._validar_nombre()
                if not nuevo_nombre:
                    print("error al actualizar nombre")
                    return False
                producto.nombre = nuevo_nombre
                print(f"Nombre del producto actualizado a {nuevo_nombre}.")
        print("el id no existe")
        return False
    #eliminar producto por id
    def eliminar_producto(self):
        validar = self.listar_productos()
        if not validar:
            return False
        id = self._validar_id()
        for producto in self.productos:
            if producto.id == id:
                self.productos.remove(producto)
                print(f"Producto {producto.nombre} eliminado con éxito.")
                return True
        print("el id no existe")
        return False

def menu():
    inventario = Inventario()
    while True:
        inventario.menu()
        opcion = input("selecione una opcion: ")
        match opcion:
            case "1":
                inventario.crear_producto()
            case "2":
                inventario.listar_productos()
            case "3":
                inventario.menu2()
                opcion2 = input("seleccione una opcion: ")
                match opcion2:
                    case "1":
                        inventario.actualizar_precio()
                    case "2":
                        inventario.actualizar_nombre()
                    case "3":
                        print("volviendo al menu principal...")
                        continue
                    case _:
                        print("opcion no valida")
                        continue
            case "4":
                inventario.eliminar_producto()
            case "5":
                print("saliendo...")
                break
            case _:
                print("opcion no valida")
                continue

menu()
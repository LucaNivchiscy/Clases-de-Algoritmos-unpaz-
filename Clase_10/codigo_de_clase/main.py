from menu import Menu
from gestor_clientes import GestorDeClientes
from gestor_productos import GestorDeProductos
from gestor_compras import GestorDeCompras

def menu_clientes(gestor_clientes: GestorDeClientes):
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


def menu_productos(gestor_productos: GestorDeProductos):
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

def menu_compras(gestor: GestorDeCompras):
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
            gestor.crear_compra()
        elif opcion == 3:
            gestor.buscar_compras_por_dni_cliente()
        elif opcion == 4:
            gestor.eliminar_compra()
        elif opcion == 5:
            gestor.guardar()
        elif opcion == 6:
            break

def main():
    gestor_productos: GestorDeProductos = GestorDeProductos("productosejemplo.bin")
    gestor_clientes: GestorDeClientes = GestorDeClientes("clientes.bin")
    gestor_compras: GestorDeCompras = GestorDeCompras("compras.bin")

    menu_principal = Menu([
        "Gestión de Productos",
        "Gestión de Clientes",
        "Gestión de Compras"
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
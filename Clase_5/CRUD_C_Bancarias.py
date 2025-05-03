"""Un banco tiene 50 cuentas. Se pide hacer un programa que realice las siguientes opciones:

ALTA: Permitir ingresa los siguientes datos de cada cuenta:
(Numero de cuenta--- entero. Tipo de cuenta --- carácter (C: cuenta corriente, A: caja de ahorro). Saldo de la cuenta --- flotante.

MODICACION: Permite cambiar el saldo de una cuenta (se busca por número de cuenta).

CONSULTA muestra los datos de todas las cuentas.

CONSULTA POR NUMERO DE CUENTA muestra los datos de una cuenta cualquiera (se busca por número de cuenta).

SALIR DEL PROGRAMA
V2:
CC-1 Se pide modificar el software  CRUD de cuentas bancarias para que permita la gestión de Clientes con los siguientes datos 
    (CUIL, nombre, apellido, fecha de nacimiento, cuentas bancarias). Cada cliente del banco puede tener múltiples cuentas.

CC-2 Se pide agregar el tipo de cuenta "cuenta sueldo"

CC-3 Se pide que cada cuenta sea en una moneda específica dentro de las cuales pueden estar: 
    ARS (pesos argentinos), USD (dólares americanos), BRL(real brasileño)"""


import re
from datetime import datetime

class Fecha:

    def __init__(self, fecha_str: str = None):
        if not fecha_str:
            hoy = datetime.now()
            self.dia = hoy.day
            self.mes = hoy.month
            self.anio = hoy.year
        else:
            # validar formato de fecha dd/mm/aaaa con expresiones regulres
            if not self.es_fecha_valida(fecha_str):
                raise ValueError('Formato de fecha no válido. Debe ser dd/mm/aaaa')
            partes = str(fecha_str).split('/')
            self.dia = int(partes[0])
            self.mes = int(partes[1])
            self.anio = int(partes[2])

    def es_fecha_valida(self, fecha: str):
        patron = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
        return re.match(patron, fecha)

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"


class Cliente:
    def __init__(self, nro_cliente: int, cuil: str, nombre: str, apellido: str, fecha_nacimiento: Fecha):
        self.nro_cliente = nro_cliente
        self.cuil =  cuil
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.cuentas: list[Cuenta] = []

    def __str__(self):
        return f"Numero de cliente: {self.nro_cliente}, CUIL: {self.cuil}, Nombre: {self.nombre}, Apellido: {self.apellido}, Fecha de Nacimiento: {self.fecha_nacimiento}"


class Cuenta:
    def __init__(self,nro_cuenta: int ,tipo_cuenta: str, saldo: float, divisa: str):
        self.nro_cuenta = nro_cuenta
        self.tipo_cuenta = tipo_cuenta
        self.saldo = saldo
        self.divisa = divisa


    def __str__(self):
        return f"Numero de cuenta: {self.nro_cuenta}, Tipo de cuenta: {self.tipo_cuenta}, Saldo: {self.saldo}$, Divisa: {self.divisa}"

class Banco:
    def __init__(self):
        self.clientes: list[Cliente] = []

    def _generar_nro_cliente(self):
        """Genera un número de cliente único"""
        if not self.clientes:
            return 1
        return max(cliente.nro_cliente for cliente in self.clientes) + 1

    def _generar_nro_cuenta(self):
        """Genera un número de cuenta único"""
        cuentas_existentes = []
        for cliente in self.clientes:
            for cuenta in cliente.cuentas:
                cuentas_existentes.append(cuenta.nro_cuenta)
        if not cuentas_existentes:
            return 1
        return max(cuentas_existentes) + 1

    """def _generar_nro_cuenta(self):
        
        for cliente in self.clientes:
            if not cliente.cuentas:
                return 1
            if cliente.cuentas:
                return max(cuenta.nro_cuenta for cuenta in cliente.cuentas) + 1"""

    def crear_cliente(self):
        """crea un cliente por medio de Class Cliente"""
        cuil = self._verificar_cuil_nro()
        nombre = input("Ingrese el nombre del cliente: ").capitalize()
        apellido = input("Ingrese el apellido del cliente: ").capitalize()
        fecha_nacimiento = Fecha(input("Ingrese la fecha de nacimiento (dd/mm/aaaa): "))
        nro_cliente = self._generar_nro_cliente()
        nuevo_cliente = Cliente(nro_cliente, cuil, nombre, apellido, fecha_nacimiento)
        self.clientes.append(nuevo_cliente)
        print("Cliente creado exitosamente.")
        input("Presione enter para continuar.")

    def _verificar_cuil_nro(self):
        """Verifica si el CUIL ingresado es un número"""
        cuil = input("Ingrese el numero de CUIL (sin guiones): ")
        if not cuil.isdigit():
            print("El CUIL debe ser un número.")
            return self._verificar_cuil_nro()
        return cuil

    def verificar_cuil(self, cuil):
        """Verifica si el CUIL ingresado corresponde a un cliente registrado"""
        for cliente in self.clientes:
            if cliente.cuil == cuil:
                return cliente
        print("El CUIL ingresado no corresponde a ningún cliente registrado.")
        input("Presione enter para continuar.")
        return False

    def crear_cuenta(self, cuil):
        """Crea una cuenta para un cliente existente"""
        tipo_cuenta =self._verificar_tipo_cuenta()
        saldo = self._verificar_saldo()
        divisa = self._verificar_divisa()
        nro_cuenta = self._generar_nro_cuenta()
        nueva_cuenta = Cuenta(nro_cuenta, tipo_cuenta, saldo, divisa)
        for cliente in self.clientes:
            if cliente.cuil == cuil:
                cliente.cuentas.append(nueva_cuenta)
                print("Cuenta creada exitosamente.")
                return

    def _verificar_tipo_cuenta(self):
        """verificar tipo de cuenta"""
        tipo_cuenta = input("Ingrese el tipo de cuenta (C: Cuenta Corriente, A: Caja de Ahorro, S: Cuenta Sueldo): ").upper()
        if tipo_cuenta not in ['C', 'A', 'S']:
            print("Tipo de cuenta no válido. Debe ser C, A o S.")
            return self._verificar_tipo_cuenta()
        if tipo_cuenta == 'C':
            return "Cuenta Corriente"
        elif tipo_cuenta == 'A':
            return "Caja de Ahorro"
        elif tipo_cuenta == 'S':
            return "Cuenta Sueldo"

    def _verificar_saldo(self):
        """verificar que saldo sea un numero positivo"""
        try:
            saldo = float(input("Ingrese el nuevo saldo de la cuenta: "))
            if saldo < 0:
                print("El saldo no puede ser negativo.")
                return self._verificar_saldo()
            return saldo
        except ValueError:
            raise ValueError("El saldo debe ser un número.")


    def _verificar_divisa(self):
        """verifica que la divisa sea una de las tres opciones"""
        divisa = input("Ingrese la divisa (1: ARS, 2: USD, 3: BRL): ")
        if divisa not in ['1', '2', '3']:
            print("Divisa no válida. Debe ser 1, 2 o 3.")
            return self._verificar_divisa()
        if divisa == '1':
            return "ARS"
        elif divisa == '2':
            return "USD"
        elif divisa == '3':
            return "BRL"

    def mostrar_cuenta(self, cuil):
        cliente = self.verificar_cuil(cuil)
        if cliente:
            print(cliente)
            if not cliente.cuentas:
                print("No hay cuentas registradas para este cliente.")
                input("Presione enter para continuar.")
                return
            for cuenta in cliente.cuentas:
                print(cuenta)

    def modificar_saldo(self, cuil):
        cliente = self.verificar_cuil(cuil)
        if cliente:
            print(cliente)
            if not cliente.cuentas:
                print("No hay cuentas resgistradas para este Cliente.")
                input("Presione enter para continuar.")
                return
            for cuenta in cliente.cuentas:
                print(cuenta)
            nro_cuenta = int(input("Ingrese el número de cuenta a modificar: "))
            for cuenta in cliente.cuentas:
                if cuenta.nro_cuenta == nro_cuenta:
                    nuevo_saldo = self._verificar_saldo()
                    cuenta.saldo = nuevo_saldo
                    print("Saldo modificado exitosamente.")
                    input("Presione enter para continuar.")
                    return
    def eliminar_cuenta(self, cuil):
        cliente = self.verificar_cuil(cuil)
        if cliente:
            print(cliente)
            if not cliente.cuentas:
                print("No hay cuentas registradas para este cliente.")
                input("Presione enter para continuar.")
                return
            for cuenta in cliente.cuentas:
                print(cuenta)
            nro_cuenta = int(input("Ingrese el número de cuenta a eliminar: "))
            for cuenta in cliente.cuentas:
                if cuenta.nro_cuenta == nro_cuenta:
                    cliente.cuentas.remove(cuenta)
                    print("Cuenta eliminada exitosamente.")
                    input("Presione enter para continuar.")
                    return



class Menu:
    def __init__(self):
        self.opciones_menu = [
            ["1. Agregar Cliente", "2. Ingresar a Cliente", "3. Salir"],
            ["1. Crear Cuenta", "2. Mostrar Datos de Cuenta", "3. Modificar saldo","4. Eliminar Cuenta", "5. Salir"]
        ]

    def mostrar_menu(self,mensaje: str, posicion_menu: int):
        print(mensaje)
        for op in self.opciones_menu[posicion_menu]:
            print(op)

    def opcion_seleccionada(self):
        opcion = input('Elegir opcion:')
        return opcion

class Aplicacion:
    def __init__(self):
        self.banco = Banco()
        self.menu = Menu()

#["1. Agregar Cliente", "2. Ingresar a Cliente", "3. Salir"],
#["1. Crear Cuenta", "2. Mostrar Datos de Cuenta", "3. Modificar saldo","4. Eliminar Cuenta", "5. Salir"]

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu("Bienvenido al Sistema de Gestion de Cuentas Bancarias", 0)
            opcion = self.menu.opcion_seleccionada()
            if opcion == '1':
                self.banco.crear_cliente()
            elif opcion == '2':
                cuil = input("Ingrese el CUIL del cliente: ")
                cliente = self.banco.verificar_cuil(cuil)
                if cliente:
                    while True:
                        self.menu.mostrar_menu(f"Bienvenido {cliente.nombre}, {cliente.apellido}",1)
                        opcion = self.menu.opcion_seleccionada()
                        if opcion == '1':
                            self.banco.crear_cuenta(cuil)
                        elif opcion == '2':
                            self.banco.mostrar_cuenta(cuil)
                        elif opcion == '3':
                            self.banco.modificar_saldo(cuil)
                        elif opcion == '4':
                            self.banco.eliminar_cuenta(cuil)
                        elif opcion == '5':
                            print("Saliendo del menu de cliente...")
                            break
            elif opcion == '3':
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

ejecutar = Aplicacion()
ejecutar.ejecutar()












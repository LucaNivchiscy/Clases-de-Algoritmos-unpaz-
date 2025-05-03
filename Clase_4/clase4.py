"""
en argentina las personas humanas pueden realiczar compras de dolares, pero hasta hace poco existia un cepo cambiario que imponia restricciones. hoy queremos simular como funcionario un sistema muy simple para registrar y proceesar este tipo de trassacciones

requisitos del ejercicio
cada compra debe registrar:
    nom, dni, mosnto en usd que desea comprar, medio de compra: homebanking o caja fisica ,fecha de la operacion
las reglas del cepo son:
    1.si el cepo esta activo no se pueden comporar mas de 200 uds por persona por mes
        si el cepo supera los 200usd y el cepo esta activo la operacion debe ser rechazada
    2.si esta desactivado no hay limite
    3. el sistema debe mostrar si la compra fue aprobada o rechazada, explicar porque y mostrar un resumen de la trasaccion realizada
"""


class Cliente:
    #La clase Cliente representa a una persona que realiza compras.
    # Cada cliente tiene un nombre, un DNI y una lista de transacciones asociadas.
    # Esta clase encapsula la información y las operaciones relacionadas con un cliente.
    def __init__(self, p_nombre, p_dni):
        self.nombre = p_nombre
        self.dni = p_dni
        self.transacciones = []

    def agregar_transaccion(self, p_monto, p_fecha):
        #permite agregar una transacción a la lista de transacciones del cliente.
        #monto y fecha
        self.transacciones.append((p_monto, p_fecha))

class Compra:
    #La clase Compra representa una transacción de compra
    #Cada compra tiene un monto, un medio de pago y una fecha asociada.
    def __init__(self, p_monto, p_medio, p_fecha):
        self.monto = p_monto
        self.medio = p_medio
        self.fecha = p_fecha

    def__str__(self):
        #Devuelve una representación en cadena de la compra.
        return f"Compra de {self.monto} USD a través de {self.medio} el {self.fecha}"

class GestionTransacciones:
    def __init__(self):
        self.clientes = []

CEPO = True
limite_cepo = 200


lista_monto = []
lista_medio = []
lista_anios = []
lista_meses = []
lista_dias = []



#funciones necesarias
def mostrar_menu():
    print("1 - Registrar compra")
    print("2 - Mostrar compras")
    print("3 - Salir")

def registrar_nombre():
    nombre = input("Ingrese su nombre: ")
    return nombre

def registrar_dni():
    dni = numero_valido("DNI: ")
    return dni

def pedir_monto():
    monto = numero_valido("Monto a comprar en USD:")
    return monto

def medio_de_compra():
    print("medios de compra validos")
    print("1 - Homebanking")
    print("2 - Caja")
    while True:
        opcion = numero_valido("elija una opcion: ")
        if opcion == 1:
            return "homebanking"
        else:
            return "caja"
"""
def fecha():
    print("ingrese una fecha en este formato dd/mm/aaaa")
    fecha = input("Ingrese la fecha: ")
    dia, mes, anio = fecha.split("/")
    dia = int(dia)
    mes = int(mes)
    anio = int(anio)
    return dia, mes, anio"""

#funciones utiles

def numero_valido(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero > 0:
                return numero
            else:
                print("El numero debe ser mayor a 0")
        else:
            print("El dato ingresado debe ser un número!")


def total_comprado(dni, mes, anio):
    total_comprado_usd = 0
    for i in range(len(lista_dni)):
        if lista_dni[i] == dni and lista_meses[i] == mes and lista_anios[i] == anio:
            total_comprado_usd = total_comprado_usd + lista_monto[i]
    return total_comprado_usd

def procesar_transacciones(nombre, dni, monto, medio, dia, mes, anio):
    monto_comprado_por_mes = total_comprado(dni, mes, anio)
    if CEPO and monto + monto_comprado_por_mes > limite_cepo:
        print(f"A superado los: {limite_cepo} USD permitdos por mes")
    else:
        lista_nombres.append(nombre)
        lista_dni.append(dni)
        lista_monto.append(monto)
        lista_medio.append(medio)
        lista_dias.append(dia)
        lista_meses.append(mes)
        lista_anios.append(anio)
        print(f"La compra de {monto} USD hecha por {nombre} (DNI: {dni}), tipo de medio: {medio}. Se realizó correctamente el {dia}/{mes}/{anio}")

def mostrar_transacciones():
    if len(lista_dni) == 0:
        print("No hay compras registradas")
    else:
        for i in range(len(lista_dni)):
            print(f"Nombre: {lista_nombres[i]}, DNI: {lista_dni[i]}, Monto: {lista_monto[i]}, Medio: {lista_medio[i]}, Fecha: {lista_dias[i]}/{lista_meses[i]}/{lista_anios[i]}")


def main():
    while True:
        mostrar_menu()
        opcion = numero_valido("Ingrese una opción: ")
        if opcion == 1:
            nombre = registrar_nombre()
            dni = registrar_dni()
            monto = pedir_monto()
            medio = medio_de_compra()
            print("ingrese la fecha de compra")
            dia = numero_valido("Dia: ")
            mes = numero_valido("Mes: ")
            anio = numero_valido("Año: ")
            procesar_transacciones(nombre, dni, monto, medio, dia, mes, anio)
        elif opcion == 2:
            print("Compras realizadas:")
            mostrar_transacciones()
        elif opcion == 3:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

main()
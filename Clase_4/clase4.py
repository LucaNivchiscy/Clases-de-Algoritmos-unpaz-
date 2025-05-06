CEPO = True
limite_cepo = 200

# Listas para guardar los datos
lista_nombres = []
lista_dni = []
lista_monto = []
lista_medio = []
lista_anios = []
lista_meses = []
lista_dias = []

# --- Clases ---
class Cliente:
    def __init__(self, p_nombre, p_dni):
        self.nombre = p_nombre
        self.dni = p_dni
        self.transacciones = []

    def agregar_transaccion(self, p_monto, p_fecha):
        self.transacciones.append((p_monto, p_fecha))


class Compra:
    def __init__(self, p_monto, p_medio, p_fecha):
        self.monto = p_monto
        self.medio = p_medio
        self.fecha = p_fecha

    def __str__(self):
        return f"Compra de {self.monto} USD a través de {self.medio} el {self.fecha}"


# --- Funciones del sistema ---
def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1 - Registrar compra")
    print("2 - Mostrar compras")
    print("3 - Salir")


def registrar_nombre():
    return input("Ingrese su nombre: ")


def numero_valido(mensaje):
    while True:
        numero = input(mensaje)
        if numero.isdigit():
            numero = int(numero)
            if numero > 0:
                return numero
            else:
                print("El número debe ser mayor a 0.")
        else:
            print("El dato ingresado debe ser un número válido.")


def registrar_dni():
    return numero_valido("DNI: ")


def pedir_monto():
    return numero_valido("Monto a comprar en USD: ")


def medio_de_compra():
    print("Medios de compra válidos:")
    print("1 - Homebanking")
    print("2 - Caja física")
    while True:
        opcion = numero_valido("Elija una opción: ")
        if opcion == 1:
            return "homebanking"
        elif opcion == 2:
            return "caja"
        else:
            print("Opción inválida. Intente nuevamente.")


def total_comprado(dni, mes, anio):
    total_comprado_usd = 0
    for i in range(len(lista_dni)):
        if lista_dni[i] == dni and lista_meses[i] == mes and lista_anios[i] == anio:
            total_comprado_usd += lista_monto[i]
    return total_comprado_usd


def procesar_transacciones(nombre, dni, monto, medio, dia, mes, anio):
    monto_comprado = total_comprado(dni, mes, anio)
    if CEPO and (monto + monto_comprado > limite_cepo):
        print(f"\n❌ Operación rechazada: supera el límite mensual de {limite_cepo} USD.")
        print(f"Ya compró {monto_comprado} USD este mes.")
    else:
        lista_nombres.append(nombre)
        lista_dni.append(dni)
        lista_monto.append(monto)
        lista_medio.append(medio)
        lista_dias.append(dia)
        lista_meses.append(mes)
        lista_anios.append(anio)
        print(f"\n✅ Compra aprobada: {monto} USD por {nombre} (DNI: {dni}) mediante {medio}.")
        print(f"Fecha: {dia}/{mes}/{anio}")


def mostrar_transacciones():
    if not lista_dni:
        print("No hay compras registradas.")
    else:
        print("\n--- TRANSACCIONES ---")
        for i in range(len(lista_dni)):
            print(f"Nombre: {lista_nombres[i]}, DNI: {lista_dni[i]}, Monto: {lista_monto[i]} USD, "
                  f"Medio: {lista_medio[i]}, Fecha: {lista_dias[i]}/{lista_meses[i]}/{lista_anios[i]}")


# --- Programa Principal ---
def main():
    while True:
        mostrar_menu()
        opcion = numero_valido("Ingrese una opción: ")
        if opcion == 1:
            nombre = registrar_nombre()
            dni = registrar_dni()
            monto = pedir_monto()
            medio = medio_de_compra()
            print("Ingrese la fecha de la compra:")
            dia = numero_valido("Día: ")
            mes = numero_valido("Mes: ")
            anio = numero_valido("Año: ")
            procesar_transacciones(nombre, dni, monto, medio, dia, mes, anio)
        elif opcion == 2:
            mostrar_transacciones()
        elif opcion == 3:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


main()

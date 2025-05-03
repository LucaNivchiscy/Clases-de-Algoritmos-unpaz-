LIMITE_CEPO = 200
CEPO_ACTIVO = True

lista_de_nombres = []
lista_de_dnis = []
lista_de_montos =[]
lista_de_medios = []
lista_de_dias = []
lista_de_meses = []
lista_de_anios = []

def mostrar_transacciones():
    for i in range(len(lista_de_dnis)):
        print(f"Transacción {i+1}: {lista_de_nombres[i]} (DNI {lista_de_dnis[i]}) monto ${lista_de_montos[i]} {lista_de_dias[i]}/{lista_de_meses[i]}/{lista_de_anios[i]}")

def mostrar_menu():
    print("---- MENU ----")
    print("1 - Procesar compra de divisas")
    print("2 - Mostrar transacciones")
    print("3 - Salir")

def pedir_numero_entero_valido(mensaje):
    entrada = input(mensaje)
    while not entrada.isnumeric():
        if entrada.isnumeric():
            break
        else:
            print("El dato ingresado debe ser un número!")
    return int(entrada)

def es_float_valido(input_str):
    try:
        float(input_str)
        return True
    except:
        return False


def pedir_numero_flotante_valido(mensaje):
    entrada=None
    while not es_float_valido(entrada):
        entrada = input(mensaje)
        if not es_float_valido(entrada):
            print("El dato ingresado debe ser un número con coma!")
    return float(entrada)

def pedir_medio_de_compra_valido():
    print("Medios de compra válidos:")
    print("1 - Homebanking")
    print("2 - Caja")
    while True:
        entrada = pedir_numero_entero_valido("Ingrese el medio o canal de compra: ")
        if entrada == 1 or entrada == 2:
            if entrada == 1:
                return "homebanking"
            else:
                return "caja"
            break
        else:
            print("Debe ingresar un medio válido")

def total_comprado_por_usuario_en_mes(dni, m, a):
    total_usd_comprado = 0
    for i in range(len(lista_de_dnis)):
        if lista_de_dnis[i] == dni and lista_de_anios[i] == a and lista_de_meses[i] == m:
            total_usd_comprado += lista_de_montos[i]
    return total_usd_comprado


def procesar_transaccion(p_comprador_dni, p_comprador_nombre, p_monto_usd, p_medio, p_dia, p_mes, p_anio):
    monto_comprado_por_usuario_por_mes = total_comprado_por_usuario_en_mes(p_comprador_dni, p_mes, p_anio)
    if CEPO_ACTIVO and p_monto_usd + monto_comprado_por_usuario_por_mes > LIMITE_CEPO:
        print(f"El monto supera el límite del cepo (${LIMITE_CEPO})")
    else:
        lista_de_nombres.append(p_comprador_nombre)
        lista_de_dnis.append(p_comprador_dni)
        lista_de_montos.append(p_monto_usd)
        lista_de_medios.append(p_medio)
        lista_de_dias.append(p_dia)
        lista_de_meses.append(p_mes)
        lista_de_anios.append(p_anio)
        print(f"La compra de ${p_monto_usd} hecha por {p_comprador_nombre} (DNI {p_comprador_dni}) se realizo correctamente el {p_dia}/{p_mes}/{p_anio}")


while True:
    mostrar_menu()
    opcion_seleccionada = pedir_numero_entero_valido("Seleccione la opción: ")
    if opcion_seleccionada == 1:
        comprador_dni = input("Ingrese el DNI del comprador: ")
        comprador_nombre = input("Ingrese el nombre del comprador: ")
        monto_usd = pedir_numero_flotante_valido("Ingrese el monto en USD")
        medio = pedir_medio_de_compra_valido()
        print("Ingrese los datos de la fecha de la compra.")
        dia = pedir_numero_entero_valido("Día: ")
        mes = pedir_numero_entero_valido("Mes: ")
        anio = pedir_numero_entero_valido("Año: ")
        procesar_transaccion(comprador_dni, comprador_nombre, monto_usd, medio, dia, mes, anio)
    elif opcion_seleccionada == 2:
        mostrar_transacciones()
    elif opcion_seleccionada == 3:
        print("Gracias!")
        break
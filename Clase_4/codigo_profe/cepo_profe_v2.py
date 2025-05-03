class GestorDeClientes:
    def __init__(self):
        self.lista_de_clientes: [ClienteDeBanco] = []

    def agregar_cliente(self, cliente):
        self.lista_de_clientes.append(cliente)

    def modificar_cliente(self, dni_cliente_a_modificar, nuevo_cliente):
        for c in self.lista_de_clientes:
            if c.dni == dni_cliente_a_modificar:
                c.nombre = nuevo_cliente.nombre
                break
    def buscar_cliente(self, dni):
        for c in self.lista_de_clientes:
            if c.dni == dni:
                return c

class ClienteDeBanco:
    def __init__(self, p_nombre, p_dni):
        self.dni = p_dni
        self.nombre = p_nombre

    def __str__(self):
        return f"{self.nombre} (DNI {self.dni})"

class Fecha:
    def __init__(self, fecha_str: str):
        fecha_split = fecha_str.split("/")
        if len(fecha_split) == 3:
            self.dia = int(fecha_split[0])
            self.mes = int(fecha_split[1])
            self.anio = int(fecha_split[2])
        else:
            raise ValueError(f"Error al crear al fecha, datos invalidos: {fecha_split}")

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.anio}"

LIMITE_CEPO = 200
CEPO_ACTIVO = False

lista_de_clientes: [ClienteDeBanco] = []
lista_de_montos =[]
lista_de_medios = []
lista_de_fechas = []

def mostrar_transacciones():
    for i in range(len(lista_de_clientes)):
        print(f"Transacción {i+1}: {lista_de_clientes[i]} monto ${lista_de_montos[i]} {lista_de_fechas[i]}")
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
    for i in range(len(lista_de_clientes)):
        if lista_de_clientes[i].dni == dni and lista_de_fechas[i].anio == a and lista_de_fechas[i].mes == m:
            total_usd_comprado += lista_de_montos[i]
    return total_usd_comprado

def procesar_transaccion(p_cliente: ClienteDeBanco, p_monto_usd: float, p_medio: str, p_fecha: Fecha):
    monto_comprado_por_usuario_por_mes = total_comprado_por_usuario_en_mes(p_cliente.dni, p_fecha.mes, p_fecha.anio)
    if CEPO_ACTIVO and p_monto_usd + monto_comprado_por_usuario_por_mes > LIMITE_CEPO:
        print(f"El monto supera el límite del cepo (${LIMITE_CEPO})")
    else:
        lista_de_clientes.append(p_cliente)
        lista_de_montos.append(p_monto_usd)
        lista_de_medios.append(p_medio)
        lista_de_fechas.append(p_fecha)
        print(f"La compra de ${p_monto_usd} hecha por {p_cliente} se realizo correctamente el {p_fecha}")


while True:
    mostrar_menu()
    opcion_seleccionada = pedir_numero_entero_valido("Seleccione la opción: ")
    if opcion_seleccionada == 1:
        comprador_dni = input("Ingrese el DNI del comprador: ")
        comprador_nombre = input("Ingrese el nombre del comprador: ")
        monto_usd = pedir_numero_flotante_valido("Ingrese el monto en USD: ")
        medio = pedir_medio_de_compra_valido()
        fecha_string = input("Ingrese la fecha de la compra (DD/MM/AAAA): ")
        fecha_transaccion = Fecha(fecha_string)
        cliente = ClienteDeBanco(comprador_nombre, comprador_dni)
        procesar_transaccion(cliente, monto_usd, medio, fecha_transaccion)
    elif opcion_seleccionada == 2:
        mostrar_transacciones()
    elif opcion_seleccionada == 3:
        print("Gracias!")
        break
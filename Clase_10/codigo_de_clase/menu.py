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
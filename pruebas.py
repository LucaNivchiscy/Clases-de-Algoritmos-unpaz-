class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


datos = Cliente("Luca","Niv")
datos.nombre = "pedro"
print(datos.nombre)
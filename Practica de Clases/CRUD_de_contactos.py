"""📌 Consigna:
Crear una clase Contacto con atributos nombre y teléfono. Luego, crear una clase Agenda que permita:

Crear (agregar) un contacto.

Leer (listar) todos los contactos.

Actualizar el teléfono de un contacto por nombre.

Eliminar un contacto por nombre.
"""

class Contacto:
    def __init__(self, nombre:str , telefono:int):
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}"

class Agenda:
    def __init__(self):
        self.contactos: list[Contacto] = []

    def menu(self):
        print("Bienvenido a la Agenda de Contactos")
        print("1. Crear contacto")
        print("2. Listar contactos")
        print("3. Actualizar contacto")
        print("4. Eliminar contacto")
        print("5. Salir")


    def crear_contacto(self):
        nombre = input("ingrese un nombre: ").capitalize()
        try:
            telefono = int(input("Ingrese un teléfono: "))
        except ValueError:
            print("Teléfono inválido. Debe ingresar solo números.")
            return

        nuevo_contacto = Contacto(nombre, telefono)
        self.contactos.append(nuevo_contacto)
        print(f"Contacto {nombre} agregado con éxito.")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
            return False
        print("Contactos en la agenda:")
        for contacto in self.contactos:
            print(f"Nombre: {contacto.nombre}, Telefono: {contacto.telefono}")
            print("-"* 20)
        return True

    def _buscar_contacto(self):
        comprueba = self.listar_contactos()
        if not comprueba:
            return False
        nombre = input("ingrese el nombre de un contacto existente: ").capitalize()
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto

    def actualizar_contacto(self):
        contacto = self._buscar_contacto()
        if not contacto:
            return
        nuevo_telefono = int(input("ingrese el nuevo telefono: "))
        contacto.telefono = nuevo_telefono
        print(f"Contacto {contacto.nombre} actualizado con éxito.")


    def eliminar_contacto(self):
        contacto = self._buscar_contacto()
        if not contacto:
            return
        print(f"Contacto {contacto.nombre} eliminado con éxito.")
        self.contactos.remove(contacto)



def main():
    agenda = Agenda()
    while True:
        agenda.menu()
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                agenda.crear_contacto()
            case "2":
                agenda.listar_contactos()
            case "3":
                agenda.actualizar_contacto()
            case "4":
                agenda.eliminar_contacto()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
main()
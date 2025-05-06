
# Descripción:
# Crea un sistema CRUD para gestionar tareas.
#   Cada tarea debe tener: ID, descripción, estado (pendiente, en progreso, completada) y prioridad (alta, media, baja).
#
# Operaciones:
#
# Agregar una tarea
#
# Ver todas las tareas
#
# Modificar una tarea (por ID)
#
# Eliminar una tarea (por ID)
#


class Tarea:
    def __init__(self, id, descripcion, estado, prioridad):
        self.id = id
        self.descripcion = descripcion
        self.estado = estado
        self.prioridad = prioridad

    def __str__(self):
        return (f"----- TAREA -----\n"
                f"📌 ID:          {self.id}\n"
                f"📝 Descripción: {self.descripcion}\n"
                f"📍 Estado:      {self.estado}\n"
                f"⭐ Prioridad:   {self.prioridad}\n"
                f"-----------------")


class GestionTarea:
    def __init__(self):
        self.tareas: list[Tarea] = []

    def _validar_si_hay_tareas(self):
        if not self.tareas:
            return False
        return True


    def _crear_id_unico(self):
        if not self._validar_si_hay_tareas():
            return 1
        return max(t.id for t in self.tareas) + 1


    def _validar_estado(self):
        while True:
            e = input("ingrese un estado de la tarea (1. Pendiente 2. En progreso 3. Completada): ")
            if e == '1':
                return "Pendiente"
            if e == '2':
                return "En progreso"
            if e == '3':
                return "Completada"
            else:
                print("Debe elegir (1,2,3) dependiendo del estado de su tarea.")
                continue

    def _validar_prioridad(self):
        while True:
            p = input("ingrese la prioridad de la tarea (1. Alta 2. Media 3. Baja): ")
            if p == '1':
                return "Alta"
            elif p == '2':
                return "Media"
            elif p == '3':
                return "Baja"
            else:
                print("Debe elegir (1,2,3) dependiendo del estado de su tarea.")
                continue



    def crear_tarea(self):
        id = self._crear_id_unico()
        descripcion = input("Ingrese una descripcion de la tarea: ")
        estado = self._validar_estado()
        prioridad = self._validar_prioridad()
        new_task = Tarea(id, descripcion, estado, prioridad)
        self.tareas.append(new_task)
        print("Tarea agendada con exito...")
        print(new_task)

    def _ver_tareas_general(self):
        if not self.tareas:
            print("No hay tareas cargadas.")
            return False
        return True

    def ver_tareas(self):
        if not self._ver_tareas_general():
            return
        for t in self.tareas:
            print(t)
        return


    def _validar_buscar_id(self):
        while True:
            id_buscar = input("Ingrese el ID de la tarea que desea encontrar: ")
            if id_buscar.isdigit():
                return int(id_buscar)
            if not id_buscar.isdigit():
                print("Ingrese un un ID numerico.")
                continue

    def ver_una_tarea(self):
        if not self._ver_tareas_general():
            return
        tarea = self._iterar_tareas()
        if not tarea:
            print("Tarea no encontrada.")
        print(tarea)

    def _iterar_tareas(self):
        id_buscar = self._validar_buscar_id()
        for t in self.tareas:
            if t.id == id_buscar:
                return t #True
        return None #False



    def modificar_tarea(self):
        if not self._ver_tareas_general():
            return
        tarea = self._iterar_tareas()
        if not tarea:
            print("TArea no encontrada.")
            return
        tarea.descripcion = input("ingrese una nueva descripcion: ")
        tarea.estado = self._validar_estado()
        tarea.prioridad = self._validar_prioridad()
        print(f"Tarea de ID: {tarea.id}, Actualizada con exito.")
        print(tarea)

    def eliminar_tarea(self):
        if not self._ver_tareas_general():
            return
        tarea = self._iterar_tareas()
        if not tarea:
            print("Tarea no encontrada.")
        self.tareas.remove(tarea)
        print(f"Tarea de ID: {tarea.id} eliminada con exito.")








class Menu:
    def __init__(self):
        # Agregar una tarea
        #
        # Ver todas las tareas
        #
        # Modificar una tarea (por ID)
        #
        # Eliminar una tarea (por ID)
        #
        self.menu = [
            "==============================",
            "         📋 MENÚ PRINCIPAL        ",
            "==============================",
            "1️⃣  Agregar una tarea.",
            "2️⃣  Ver todas las tareas.",
            "3️⃣  Ver una tarea (ingresar ID).",
            "4️⃣  Modificar una tarea (ingresar ID).",
            "5️⃣  Eliminar una tarea (ingresar ID).",
            "6️⃣  Salir del programa.",
            "=============================="
        ]

    def mostrar_menu(self):
        for op in self.menu:
            print(op)
        return
    def solicitar_op(self):
        op = input("ingrese una opocion: ")
        return op

class Aplicacion:
    def __init__(self):
        self.gestion_tarea = GestionTarea()
        self.menu = Menu()

    def ejecutar(self):
        while True:
            self.menu.mostrar_menu()
            op = self.menu.solicitar_op()
            match op:
                case '1':
                    self.gestion_tarea.crear_tarea()
                case '2':
                    self.gestion_tarea.ver_tareas()
                case '3':
                    self.gestion_tarea.ver_una_tarea()
                case '4':
                    self.gestion_tarea.modificar_tarea()
                case '5':
                    self.gestion_tarea.eliminar_tarea()
                case '6':
                    print("Saliendo del prgrama...")
                    break
                case _:
                    print("Ingrese una opcion valida (1,2,3,4,5 6)")


app = Aplicacion()
app.ejecutar()





















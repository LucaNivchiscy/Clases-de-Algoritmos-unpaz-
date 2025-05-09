

# Descripción:
# Crea un sistema para gestionar libros y usuarios de una biblioteca. Los usuarios pueden tomar prestado o devolver libros.
# Cada libro tiene: ID, título, autor, disponibilidad
# Cada usuario tiene: ID, nombre, libros_prestados


class Libro:
    def __init__(self, id: int, titulo: str, autor: str, disp: bool):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disp = disp

    # python
    def __str__(self):
        return f"\033[1;34mID:\033[0m {self.id} | \033[1;32mTítulo:\033[0m \"{self.titulo}\" | \033[1;33mAutor:\033[0m {self.autor}"


class Usuario:
    def __init__(self, id: int, nombre: str):
        self.id = id
        self.nombre = nombre
        self.libros_prestados = []

    def __str__(self):
        return f"\033[1;34mID:\033[0m {self.id} | \033[1;32mNombre:\033[0m \"{self.nombre}\" | \033[1;33mLibros prestados:\033[0m {len(self.libros_prestados)}"

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def _crear_id(self):
        if not self.libros:
            return 1
        return max(l.id for l in self.libros) + 1

    def _crear_id_usuario(self):
        if not self.usuarios:
            return 1
        return max(u.id for u in self.usuarios) + 1

    def crear_usuario(self):
        id = self._crear_id_usuario()
        nombre = input("Ingrese el nombre del usuario: ").capitalize()
        new_user = Usuario(id, nombre)
        self.usuarios.append(new_user)
        print(f"Usuario creado: {new_user}")



    def agregar_libro(self):
        id = self._crear_id()
        titulo = input("Ingrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        disp = True
        new_book = Libro(id, titulo, autor, disp)
        self.libros.append(new_book)
        print(f"Libro agregado: {new_book}")

    def solicitar_libros(self):
        if not self.usuarios:
            print("No hay usuarios registrados.")
            return False
        if not self.libros:
            print("No hay libros disponibles.")
            return False
        id_usuario = int(input("Ingrese el ID del usuario: "))
        for usuario in self.usuarios:
            if usuario.id == id_usuario:
                break
        else:
            print("Usuario no encontrado.")
            return False

        id_libro = int(input("Ingrese el ID del libro: "))
        for libro in self.libros:
            if libro.id == id_libro and libro.disp:
                libro.disp = False
                usuario.libros_prestados.append(libro)
                print(f"Libro prestado: {libro}")
                return True
        else:
            print("Libro no disponible o no encontrado.")
            return False






















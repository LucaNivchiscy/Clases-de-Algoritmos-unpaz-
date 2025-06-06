

class Medico:
    def __init__(self, matricula:str ,nombre: str, especialidad: str):
        if not matricula.isdigit() or len(matricula) < 5:
            raise ValueError("La matrícula debe ser numérica y tener al menos 5 dígitos.")
        self.matricula = matricula
        self.nombre = nombre
        self.especialidad = especialidad


    def __str__(self):
        return (f"--- DATOS DEL MÉDICO ---\n"
                f"  - Nombre: {self.nombre}\n"
                f"  - Matrícula: {self.matricula}\n"
                f"  - Especialidad: {self.especialidad}\n"  
                f"------------------------")
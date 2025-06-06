import os
from menu import Menu
from gestion_de_pacientes import GestionDePacientes
from gestion_de_medicos import GestionDeMedicos
from gestion_de_turnos import GestionDeTurnos



def menu_pacientes(gestion_de_pacientes: GestionDePacientes):
    menu = Menu([
        "Listar Pacientes",
        "Buscar paciente por DNI",
        "Agregar paciente",
        "Modificar paciente",
        "Eliminar Paciente",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestion_de_pacientes.listar_pacientes()
        elif opcion == 2:
            gestion_de_pacientes.buscar_paciente()
        elif opcion == 3:
            gestion_de_pacientes.agregar_paciente()
        elif opcion == 4:
            gestion_de_pacientes.modificar_paciente()
        elif opcion == 5:
            gestion_de_pacientes.eliminar_paciente()
        elif opcion == 6:
            gestion_de_pacientes.guardar_cambios()
        elif opcion == 7:
            break


def menu_medicos(gestion_de_medicos: GestionDeMedicos):
    menu = Menu([
        "Listar Médicos",
        "Buscar Médico por matricula",
        "Agregar Medico",
        "Modificar Medico",
        "Eliminar Medico",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestion_de_medicos.listar_medicos()
        elif opcion == 2:
            gestion_de_medicos.buscar_medico()
        elif opcion == 3:
            gestion_de_medicos.agregar_medico()
        elif opcion == 4:
            gestion_de_medicos.modificar_medico()
        elif opcion == 5:
            gestion_de_medicos.eliminar_medico()
        elif opcion == 6:
            gestion_de_medicos.guardar_cambios()
        elif opcion == 7:
            break

def menu_turnos(gestion_de_turnos: GestionDeTurnos):
    menu = Menu([
        "Listar Turnos",
        "Listar turnos por Paciente o Médico",
        "Buscar por Fecha",
        "Agregar Turno",
        "Eliminar Turno",
        "Guardar cambios",
        "Volver al menú principal"
    ])
    while True:
        menu.mostrar()
        opcion = menu.pedir_opcion()

        if opcion == 1:
            gestion_de_turnos.listar_turnos()
        elif opcion == 2:
            gestion_de_turnos.listar_paciente_medico()
        elif opcion == 3:
            gestion_de_turnos.buscar_por_fecha()
        elif opcion == 4:
            gestion_de_turnos.agregar_turno()
        elif opcion == 5:
            gestion_de_turnos.eliminar_turno()
        elif opcion == 6:
            gestion_de_turnos.guardar_cambios()
        elif opcion == 7:
            break

def main():
    os.makedirs("Datos", exist_ok=True)  # Asegura que el directorio "Datos" exista
    gestion_de_pacientes: GestionDePacientes = GestionDePacientes("Datos/pacientes.bin")
    gestion_de_medicos: GestionDeMedicos = GestionDeMedicos("Datos/medicos.bin")
    gestion_de_turnos: GestionDeTurnos = GestionDeTurnos("Datos/turnos.bin", gestion_de_pacientes, gestion_de_medicos)
    # para poder eliminar los turnos de pacientes y medicos eliminados
    gestion_de_pacientes.gestion_de_turnos = gestion_de_turnos
    gestion_de_medicos.gestion_de_turnos = gestion_de_turnos

    menu_principal = Menu([
        "Gestión de Pacientes",
        "Gestión de Medicos",
        "Gestión de Turnos",
        "Salir"
    ])

    while True:
        menu_principal.mostrar()
        opcion = menu_principal.pedir_opcion()
        if opcion == 1:
            menu_pacientes(gestion_de_pacientes)
        elif opcion == 2:
            menu_medicos(gestion_de_medicos)
        elif opcion == 3:
            menu_turnos(gestion_de_turnos)
        elif opcion == 4:
            print("Saliendo del programa...")
            break


main()




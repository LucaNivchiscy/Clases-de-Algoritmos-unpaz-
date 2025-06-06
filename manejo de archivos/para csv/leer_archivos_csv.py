

import csv
# #Leer un archivo CSV
# with open("alumnos.csv", "r", newline='') as archivo:
#     lector = csv.reader(archivo)
#     for fila in lector:
#         print(fila)  # ['Juan', '25', '8']
#
# #Si quiero saltar el encabezado
# with open("alumnos.csv", "r", newline='') as archivo:
#     lector = csv.reader(archivo)
#     next(lector)  # Salta la primera línea
#     for fila in lector:
#         print(fila)

#Escribir un archivo CSV
# with open("alumnos.csv", "w", newline='') as archivo:
#     escritor = csv.writer(archivo)
#     escritor.writerow(["nombre", "edad", "nota"])  # Encabezado
#     escritor.writerow(["Juan", 25, 8])
#     escritor.writerow(["Ana", 30, 9])

# with open("alumnos.csv", "a", newline='') as archivo:
#     escritor = csv.writer(archivo)
#     escritor.writerow(["Luis", 22, 7])


#Escribir un archivo CSV con diccionarios

with open("alumnos.csv", "w", newline='') as archivo:
    campos = ["nombre", "edad", "nota"]
    escritor = csv.DictWriter(archivo, fieldnames=campos)

    escritor.writeheader()
    escritor.writerow({"nombre": "Juan", "edad": 25, "nota": 8})
    escritor.writerow({"nombre": "Ana", "edad": 30, "nota": 9})

#Leer un archivo CSV con diccionarios

with open("alumnos.csv", "r", newline='') as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(f"{fila['nombre']} tiene {fila['edad']} años y sacó {fila['nota']}")



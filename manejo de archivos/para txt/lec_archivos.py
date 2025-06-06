
## Manejo de Archivos en Python

## En Python, el manejo de archivos se realiza a través de la función open(), que permite abrir un archivo y realizar operaciones sobre él.
## La función open() recibe dos parámetros: el nombre del archivo y el modo de apertura.
## Los modos de apertura más comunes son:
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip())

print("\n\n")

with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)


## Escribir en un archivo
with open("nuevo.txt", "w") as archivo:
    archivo.write("Hola mundo\n")
    archivo.write("Segunda línea\n")

with open("nuevo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

#agregar contenido a un archivo, est
# with open("archivo.txt", "a") as archivo:
#     archivo.write("Carlos,28\n")
# with open("archivo.txt", "r") as archivo:
#     contenido = archivo.read()
#     print(contenido)

#Actualizar contenido de un archivo (leer, modificar y sobreescribir)
# Leer líneas
with open("archivo.txt", "r") as archivo:
    lineas = archivo.readlines()

# Modificar (por ejemplo, cambiar la edad de Ana)
for i in range(len(lineas)):
    if lineas[i].startswith("Ana"):
        lineas[i] = "Ana,35\n"

# Sobrescribir con los nuevos datos
with open("archivo.txt", "w") as archivo:
    archivo.writelines(lineas)


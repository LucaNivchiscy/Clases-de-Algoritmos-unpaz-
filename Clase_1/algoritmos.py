"escribir el algoritmo para calcular el factorial de caulquier numero de manera iterativa"
"""num = 7
acumulador = 1
for n in range(acumulador, num+1):
    acumulador = acumulador * n

print(acumulador)

def factorial(numero):
    acum = 1
    for i in range(acum, numero +1):
       acum = acum * i
    return print(acum)
numero = int(input("numero: "))
factorial(numero)



base = 2
exponente = 3
potencia = base
for i in range(exponente-1):
    potencia = potencia * base
print(potencia)
"""

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente-1)

print(potencia(2,3))
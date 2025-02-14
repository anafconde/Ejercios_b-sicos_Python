#Ejercicio 14
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.

numero = int(input("Introduce un número: "))

cifra_unidades = numero % 10
cifra_decenas = numero // 10

numero_invertido = cifra_unidades * 10 + cifra_decenas
print(numero_invertido)
#Ejercicio 13
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero=int(input("Indica un número para ver su raíz cuadrada y cúbica: "))

import math
raiz_cuadrada=math.sqrt(numero)

raiz_cubica=(numero ** 1/3)

print(f"La raíz cuadrada de {numero} es: {raiz_cuadrada}")

print(f"La raíz cúbica de {numero} es: {raiz_cubica}")
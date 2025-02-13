

# Author = Iván Suárez
# Version = 1.0
# Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

from math import sqrt, cbrt

num = float(input("Introduce un valor positivo: "))

sqr = sqrt(num)
cbr = cbrt(num)

print(f"Del número {num} su raiz cuadrada es {sqr} y la cúbica es {cbr}")
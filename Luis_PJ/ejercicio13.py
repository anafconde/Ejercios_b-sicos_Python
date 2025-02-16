# Author: Luis Palacios
# Version: 1.0
# Ejercicio 13 Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

import math

numero=float(input("Indicame un numero: "))
raizcuadrada=math.sqrt(numero)
raizcubica=math.cbrt(numero)

print("La raiz cuadrada de",numero,"es",raizcuadrada,"y la raíz cúbica es",raizcubica)
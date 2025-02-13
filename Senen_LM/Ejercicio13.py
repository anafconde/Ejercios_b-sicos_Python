#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

#version 1.0
#author Senén Lara

import math

n1=int(input("Introduce tu numero: "))
n1cuadrado=math.sqrt(n1)
n1cubica=math.cbrt(n1)

print("La raiz cuadrada de tu numero es: ",n1cuadrado ,"Y la cubica es: ",n1cubica)
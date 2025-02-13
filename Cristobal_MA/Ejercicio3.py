#Autor: Cris Moreno
#Version: 1.0
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1=float(input("Dime el primer cateto: "))
cateto2=float(input("Dime el segundo cateto: "))
catsuma=(cateto1*cateto1)+(cateto2*cateto2)
hipotenusa=math.sqrt(catsuma)
print("La hipotenusa de tu triangulo",hipotenusa)
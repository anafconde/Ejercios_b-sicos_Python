#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
#version 1.0
#author Senén Lara

import math

c1=int(input("Introduce el primer cateto: "))
c2=int(input("Introduce el segundo cateto: "))

cateto1=c1**2
cateto2=c2**2
suma=cateto2+cateto1
hipotenusa= math.sqrt(suma)
print("La hipotenusa es ", hipotenusa)
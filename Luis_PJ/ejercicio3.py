# Author: Luis Palacios
# Version: 1.0
# Ejercicio 2 Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

import math

cateto1=float(input("Dime el valor del primer cateto: "))
cateto2=float(input("Dime el valor del segundo cateto: "))
discriminante=(cateto1*cateto1)+(cateto2*cateto2)
hipotenusa=math.sqrt(discriminante)
print("El valor de la hipotenusa es",hipotenusa)



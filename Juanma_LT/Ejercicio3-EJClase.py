#Ejercicio 3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1=float(input("Indica el primer número: "))
cateto2=float(input("Indica el segundo número: "))

import math
hipotenusa=math.sqrt(cateto1**2 + cateto2**2)

print(f"El resultado es: {hipotenusa}")
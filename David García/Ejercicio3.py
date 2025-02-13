#Ejercicio 3
#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.

cateto_a = float(input("Introduce la longitud del primer cateto: "))
cateto_b = float(input("Introduce la longitud del segundo cateto: "))

hipotenusa = (cateto_a**2 + cateto_b**2)**0.5

print("La hipotenusa del triángulo rectángulo es: " , hipotenusa)
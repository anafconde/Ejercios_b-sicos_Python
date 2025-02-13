# Author: Luis Palacios
# Version: 1.0
# Ejercicio 7 Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos=int(input("Dime una cantidad en minutos: "))
horas=minutos//60
minutos2=minutos%60

print(minutos,"minutos son",horas,"horas y",minutos2,"minutos")
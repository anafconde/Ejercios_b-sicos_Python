# Author: Luis Palacios
# Version: 1.0
# Ejercicio 5 Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
# C = (-3F2)*5/9

Fahrenheit=float(input("Dime la temperatura en grados Fahrenheit: "))
celsius=((Fahrenheit-32)*(5/9))
print(Fahrenheit,"º Fahrenheit es en º Celsius:",celsius)
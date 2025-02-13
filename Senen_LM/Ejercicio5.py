#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es:
#C = (F-32)*5/9

#version 1.0
#author Senén Lara

gradosf=int(input("Introduce los grados farenheit: "))
gradosc=(gradosf-32)*5/9
print("Tus grados en celsius son",gradosc)
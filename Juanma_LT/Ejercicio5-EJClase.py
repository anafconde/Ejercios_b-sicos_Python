#Ejercicio 5
#Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius. Recordar que la fórmula para la conversión es: C = (F-32)*5/9
grados_f=float(input("Indica el número de grados Fahrenheit: "))
grados_c=((grados_f - 32)* 5 / 9)

print(f"La equivalencia a grados Celsius es a: {grados_c}ºC")

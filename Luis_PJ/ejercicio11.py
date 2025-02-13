# Author: Luis Palacios
# Version: 1.0
# Ejercicio 11 Pide al usuario dos números y muestra la “distancia” entre ellos 
# (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

numero1=float(input("Dime un numero: "))
numero2=float(input("Dime un numero: "))

distancia=abs(numero1-numero2)
print("La distancia entre los dos puntos es:", distancia)
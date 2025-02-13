#autor:Richard Bustamante Carreño
#version:1.0

#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

import math

x1 = float(input("Dime x1: "))
x2 = float(input("Dime x2: "))
y1 = float(input("Dime y1: "))
y2 = float(input("Dime y2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print("La distancia entre los puntos es: ", distancia)
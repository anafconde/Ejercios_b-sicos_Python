# Alvaro Luzon Muñoz
#---version 1.0----
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.



import math


x1 = float(input("Ingrese la coordenada x1: "))
y1 = float(input("Ingrese la coordenada y1: "))
x2 = float(input("Ingrese la coordenada x2: "))
y2 = float(input("Ingrese la coordenada y2: "))

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia:.2f}")

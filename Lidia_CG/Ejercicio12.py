#Lidia Castro Gutiérrez
#Versión 1

# 12. Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.

import math


x1=float(input("Dime la coordenada x1 del primer punto:"))
y1=float(input("Dime la coordenada y1 del primer punto:"))

x2=float(input("Dime la coordenada x2 del segundo punto:"))
y2=float(input("Dime la coordenada y2 del segundo punto:"))

distancia=math.sqrt(((x2-x1)**2)+((y2+y1)**2))

print(f"La distancia entre ellos es {distancia}")
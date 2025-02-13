#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos
import math

x1=float(input("Introduce las coordenadas del primer punto (1) "))
y1=float(input("Introduce las coordenadas del primer punto (2) "))

x2=float(input("Introduce las coordenadas del segundo punto (1) "))
y2=float(input("Introduce las coordenadas del segundo punto (2) "))

res=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print(f"La distancia entre los dos puntos es: {res}")
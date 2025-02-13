#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.
import math
print("Introduce las coordenadas el primer punto")
x1=float(input("X: "))
y1=float(input("Y: "))
print("Introduce las coordenadas el segundo punto")
x2=float(input("X: "))
y2=float(input("Y: "))

res=math.sqrt(((x2-x1)**2)+((y2-y1)**2))

print(f"El resultado es: {res}")
# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado:  Ejercicio 12: Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos en el plano. Calcula y muestra la distancia entre ellos.


x1 = float(input("Ingresa la coordenada x1: "))
y1 = float(input("Ingresa la coordenada y1: "))
x2 = float(input("Ingresa la coordenada x2: "))
y2 = float(input("Ingresa la coordenada y2: "))


distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5  


print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia}")

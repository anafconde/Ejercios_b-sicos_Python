#Autor
#Version
#Enunciado

d = float(input("Ingrese la distancia entre los dos vehículos (km): "))

v1 = float(input("Ingrese la velocidad del primer vehículo (km/h): "))

v2 = float(input("Ingrese la velocidad del segundo vehículo (km/h): "))

tiempohoras = d / (v2 - v1)

tiempominutos = tiempohoras * 60

print(f"El vehículo más rápido alcanzará al otro en {tiempominutos:.2f} minutos.")


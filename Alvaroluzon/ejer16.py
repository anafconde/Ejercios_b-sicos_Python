# Alvaro Luzon Muñoz
#---version 1.0----
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.



d = float(input("Ingrese la distancia entre los vehículos (km): "))
v1 = float(input("Ingrese la velocidad del vehículo adelante (km/h): "))
v2 = float(input("Ingrese la velocidad del vehículo detrás (km/h): "))

minutos = (d / (v2 - v1)) * 60
minutos = max(minutos, float('inf'))

print(f"El vehículo alcanzará al otro en {minutos:.2f} minutos.")
#autor:Richard Bustamante Carreño
#version:1.0

#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia = float(input("Introduce la distancia entre los vehiculos: "))
velocidad1 = float(input("Cual es la velocidad del primer vehiculo"))
velocidad2 = float(input("Cual es la velocidad del segundo vehiculo"))

tiempo = (distancia / (velocidad2 - velocidad1))*60

print(f"Los vehiculos se encontarran a los {tiempo} minutos")
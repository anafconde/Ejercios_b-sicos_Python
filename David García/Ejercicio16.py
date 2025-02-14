#Ejercicio 16
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

distancia = float(input("Introduce la distancia entre los vehículos (km): "))
velocidad1 = float(input("Introduce la velocidad del vehículo más lento (km/h): "))
velocidad2 = float(input("Introduce la velocidad del vehículo más rápido (km/h): "))

velocidad_relativa = velocidad2 - velocidad1
tiempo_horas = distancia / velocidad_relativa
tiempo_minutos = tiempo_horas * 60

print("El vehículo más rápido alcanzará al otro en", tiempo_minutos, "minutos.")
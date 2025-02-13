#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

#Pedir los datos necesarios
dist=float(input("Introduce la distancia en KM: "))
v1=float(input("Introduce la velocidad del primer coche: "))
v2=float(input("Introduce la velocidad del segundo coche: "))

#Calcula el tiempo en minutos
time=(dist/(v2-v1))*60

#Muestra el resultado
print(f"Tardará {time} minutos.")


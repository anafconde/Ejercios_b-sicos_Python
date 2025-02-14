#Lidia Castro Gutiérrez
#Versión 1

#16. Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.

d = float(input("Dime la distancia entre los dos vehículos (km): "))
v1 = float(input("Dime la velocidad del vehículo más rápido (km/h): "))
v2 = float(input("Dime la velocidad del vehículo más lento (km/h): "))

#tiempo = distancia/velocidad

tiempo=(d/(v1-v2))*60

print(f"El vehículo más rápido alcanzará al más lento en {tiempo} minutos")
#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro

v1=float(input("Introduce la velocidad del primer vehículo: "))
v2=float(input("Introduce la velocidad del segundo vehículo (irá más rápido): "))
d=float(input("Introduce la distancia inicial entre ambos: "))

tiempo=(d/(v2-v1))*60

print(f"El tiempo que tardará el vehículo 2 en alcanzar el 1 serán {tiempo} minutos")
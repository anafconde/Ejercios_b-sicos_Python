# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado:  Ejercicio 16: Dos vehículos viajan a diferentes velocidades (v1 y v2) y están distanciados por una distancia d. El que está detrás viaja a una velocidad mayor. Se pide hacer un algoritmo para ingresar la distancia entre los dos vehículos (km) y sus respectivas velocidades (km/h) y con esto determinar y mostrar en que tiempo (minutos) alcanzará el vehículo más rápido al otro.


d = float(input("Ingrese la distancia entre los vehículos : "))
v1 = float(input("Ingrese la velocidad del vehículo más lento : "))
v2 = float(input("Ingrese la velocidad del vehículo más rápido : "))


tiempo_horas = d / (v2 - v1)  
tiempo_minutos = tiempo_horas * 60  


print(f"El vehículo más rápido alcanzará al más lento en {tiempo_minutos} minutos.")

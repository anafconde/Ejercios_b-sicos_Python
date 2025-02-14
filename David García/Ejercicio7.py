#Ejercicio 7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

minutos = int(input("Introduce la cantidad de minutos: "))

horas = minutos // 60
minutos_restantes = minutos % 60

print("{} minutos son {} horas y {} minutos.".format(minutos, horas, minutos_restantes))
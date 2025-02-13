#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. 
#Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
#version 1.0
#author Senén Lara

minutos=float(input("Introduce los minutos: "))
horas=minutos//60
minutos2=minutos%60
print("Tus minutos son: ", horas, "horas y ", minutos2, "Minutos")



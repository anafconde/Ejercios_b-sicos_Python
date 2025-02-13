

# Author = Iván Suárez
# Version = 1.0
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.

input = int(input("Introduce un número entero: "))
hour = input//60
min = 1000-(hour*60)


print(f"Son {hour} horas {min} minutos")
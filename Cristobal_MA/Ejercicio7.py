#Autor: Cris Moreno
#Version: 1.0
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
#cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 
#minutos.

minutos=int(input("Dime los minutos a transformar: "))
horas=(minutos//60)
min=(minutos%60)
print(minutos,"minutos son",horas,"horas y",min,"minutos" )


#Ejercicio 7
#Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
minutos=int(input("Indica el número de minutos que quiere señalar y calcular: "))

hora=(minutos /60)
minutos_sobrantes=(minutos %60)

print(f"El número de {minutos} minutos señalado indica {hora} horas y {minutos_sobrantes} minutos")

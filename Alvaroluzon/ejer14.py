# Alvaro Luzon Muñoz
#---version 1.0----
#Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido. Ejemplo, si se introduce 23 que muestre 32.




num = int(input("Ingrese un número de dos cifras: "))


num2 = num % 10 
decena = num // 10 
num3 = (num2 * 10) + decena

print(f"El número invertido es: {num3}")

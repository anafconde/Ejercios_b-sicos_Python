#Autor
#Version
#Enunciado

num = int(input("Ingrese un número de dos cifras: "))

decenas = num // 10  
unidades = num % 10 

invertido = (unidades * 10) + decenas

print(f"El número invertido es: {invertido}")

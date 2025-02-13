#Pide al usuario dos números y muestra la “distancia” entre ellos 
#(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

#version 1.0
#author Senén Lara

n1=float(input("Introduce el primer numero: "))
n2=float(input("Introduce el segundo numero: "))
distancia=n1-n2
distanciareal=abs(distancia)
print("La distancia es: ", distanciareal)
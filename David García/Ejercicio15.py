#Ejercicio 15
#Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

A = int(input("Introduce el valor de A: "))
B = int(input("Introduce el valor de B: "))

auxiliar = A
A = B
B = auxiliar

print("El valor de A es:", A)
print("El valor de B es:", B)
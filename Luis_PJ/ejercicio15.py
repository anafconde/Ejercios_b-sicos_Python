# Author: Luis Palacios
# Version: 1.0
# Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al final las dos variables.

a=int(input("Introduce el valor de A: "))
b=int(input("Introduce el valor de B: "))

print("La variable A vale:",a,"y la variable B vale:",b)
a, b=b, a
print("Intercambiamos sus valores. A =",a,"B =",b)
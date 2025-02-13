

# Author = Iván Suárez
# Version = 1.0
# Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).

n1 = float(input("Introduce el primer valor: "))
n1 -= float(input("Introduce el segundo valor: "))

n1=abs(n1)

print(f"Entre los dos hay {n1} metros de distancia")

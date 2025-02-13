#Ejercicio 11
#Pide al usuario dos números y muestra la “distancia” entre ellos (el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).
numero1=int(input("Indique el primer número: "))
numero2=int(input("Indique el segundo número: "))

distancia=abs(numero1 - numero2)

print(f"La distancia entre {numero1} y {numero2} es de: {distancia}")
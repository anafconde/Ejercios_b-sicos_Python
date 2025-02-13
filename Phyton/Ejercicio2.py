# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado: Ejercicio 2: Calcular el área y el perímetro de un rectángulo dados su base y altura.


base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))


area = base * altura
perimetro = 2 * base + 2 * altura


print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")

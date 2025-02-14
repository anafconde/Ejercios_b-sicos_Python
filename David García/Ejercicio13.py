#Ejercicio 13
#Realizar un algoritmos que lea un número y que muestre su raíz cuadrada y su raíz cúbica.

numero = float(input("Introduce un número: "))

raiz_cuadrada = numero ** 0.5
print("La raíz cuadrada de", numero, "es:", raiz_cuadrada)

raiz_cubica = numero ** (1/3)
print("La raíz cúbica de", numero, "es:", raiz_cubica)


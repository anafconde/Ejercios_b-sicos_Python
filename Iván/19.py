

# Author = Iván Suárez
# Version = 1.0
# Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.


co = int(input("¿Cuántas respuestas correctas?: "))
inco = int(input("¿Cuántas respuestas incorrectas?: "))
blank = int(input("¿Cuántas respuestas en blanco?: "))
res = co*5
res -= inco

print(f"La puntuación final son {res} puntos con {blank} respuestas en blanco")
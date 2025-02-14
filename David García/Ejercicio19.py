#Ejercicio 19
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

respuestas_correctas = int(input("Introduce el número de respuestas correctas: "))
respuestas_incorrectas = int(input("Introduce el número de respuestas incorrectas: "))
respuestas_en_blanco = int(input("Introduce el número de respuestas en blanco: "))

puntuacion_correcta = respuestas_correctas * 5
puntuacion_incorrecta = respuestas_incorrectas * -1
puntuacion_en_blanco = respuestas_en_blanco * 0

nota_final = puntuacion_correcta + puntuacion_incorrecta + puntuacion_en_blanco

nota_definitiva = nota_final / 10

print("La nota final del estudiante es:", nota_definitiva)
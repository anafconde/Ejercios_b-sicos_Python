#Escribir un algoritmo para calcular la nota final de un estudiante, 
#considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. 
#Imprime el resultado obtenido por el estudiante.

#version 1.0
#author Senén Lara

correctas=int(input("Introduce el numero de respuestas correctas: "))
incorrectas=int(input("Introduce el numero de respuestas incorrectas: "))
blanco=int(input("Introduce el numero de respuestas en blanco: "))

puntoscorrectas=correctas*5
puntosincorrectas=incorrectas*(-1)
notafinal=puntoscorrectas+puntosincorrectas
print("El alumno ha sacado: ", notafinal, "puntos")

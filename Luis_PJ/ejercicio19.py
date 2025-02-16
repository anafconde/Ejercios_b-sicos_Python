# Author: Luis Palacios
# Version: 1.0
#Escribir un algoritmo para calcular la nota final de un estudiante, considerando que: por cada respuesta correcta 5 puntos, por una incorrecta -1 y por respuestas en blanco 0. Imprime el resultado obtenido por el estudiante.

rcorrecta=int(input("Introduce el numero de respuestas correctas: "))
rincorrecta=int(input("Introduce el numero de respuestas incorrectas: "))
rblanco=int(input("Introduce el numero de respuestas en blanco: "))

puntorescorrecta=rcorrecta*5
puntorincorrecta=rincorrecta*(-1)
nota=puntorescorrecta+puntorincorrecta
print("La nota final del alumnos es:",nota)
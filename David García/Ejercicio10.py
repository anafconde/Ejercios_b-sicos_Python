#Ejercicio 10
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial1 = float(input("Ingresa la calificación del primer parcial: "))
parcial2 = float(input("Ingresa la calificación del segundo parcial: "))
parcial3 = float(input("Ingresa la calificación del tercer parcial: "))

examen_final = float(input("Ingresa la calificación del examen final: "))

trabajo_final = float(input("Ingresa la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print("La calificación final del alumno es:", calificacion_final)

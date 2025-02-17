# Alvaro Luzon Muñoz
#---version 1.0----
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial1 = float(input("Ingrese la primera calificación parcial : "))
parcial2 = float(input("Ingrese la segunda calificación parcia2 : "))
parcial3 = float(input("Ingrese la tercera calificación parcia3 : "))

examenF = float(input("Ingrese la calificación del examen final : "))

trabajoF = float(input("Ingrese la calificación del trabajo final : "))

promedioP = (parcial1 + parcial2 + parcial3) / 3

calificacionF = (promedioP * 0.55) + (examenF * 0.30) + (trabajoF * 0.15)

print("La calificación final es: ", calificacionF)

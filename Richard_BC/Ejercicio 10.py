#autor:Richard Bustamante Carreño
#version:1.0


# Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parciales = float(input("Pon tu calificacion parcial 1/3: "))
parciales2 = float(input("Pon tu calificacion parcial 2/3: "))
parciales3 = float(input("Pon tu calificacion parcial 3/3: "))
examfinal = float(input("Dime la calificacion de tu examen final: "))
trafinal = float(input("Dime la calificacion final del curso: "))

resultado = (((parciales+parciales2+parciales3)/3)*0.55)+(examfinal*0.3)+(trafinal*0.15)

print("Tu calificacion final del curso es: ", resultado)
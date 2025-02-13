#---------------Autor: inesmariabp---------------#
#---------------Version: 1.0---------------------#
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

#Pedir las calificaciones
ex1=float(input("Introduce la nota del primer examen: "))
ex2=float(input("Introduce la nota del segundo examen: "))
ex3=float(input("Introduce la nota del tercer examen: "))
exf=float(input("Introduce la nota del examen final: "))
tra=float(input("Introduce la nota del trabajo: "))

mex=(ex1+ex2+ex3)/3
nota=(mex*0.55)+(exf*0.3)+(tra*0.15)
print(f"La nota final es: {nota}")
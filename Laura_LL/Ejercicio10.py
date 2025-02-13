#-----Autor:LauraLinares---
#-----Version:V1-----------
#---Enunciado del algoritmo
#Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial1=float(input("Introduce la nota del primer parcial: "))
parcial2=float(input("Introduce la nota del segundo parcial: "))
parcial3=float(input("Introduce la nota del tercer parcial: "))

examen=float(input("Introduce la nota del examen final: "))

trabajo=float(input("Introduce la nota del trabajo final: "))

media=(parcial1+parcial2+parcial3)/3
parciales=media*0.55
nota=parciales+(examen*0.3)+(trabajo*0.15)

print(f"La nota final de la asignatura Algoritmos es: {nota}")
# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado: Ejercicio 10: Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

#55% del promedio de sus tres calificaciones parciales.
#30% de la calificación del examen final.
#15% de la calificación de un trabajo final.

parcial1 = float(input("Ingresa la nota del primer parcial: "))
parcial2 = float(input("Ingresa la nota del segundo parcial: "))
parcial3 = float(input("Ingresa la nota del tercer parcial: "))

examen_final = float(input("Ingresa la nota del examen final: "))
trabajo_final = float(input("Ingresa la nota del trabajo final: "))

Nota_Final = ((( parcial1 + parcial2 + parcial3 ) /3) * 55 ) / 100 + (examen_final *30) / 100 + (trabajo_final * 15) / 100

print(f"la nota final es : {Nota_Final}")


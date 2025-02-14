#Lidia Castro Gutiérrez
#Versión 1

# 10.Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:

    #55% del promedio de sus tres calificaciones parciales.
    #30% de la calificación del examen final.
    #15% de la calificación de un trabajo final.

parcial1=float(input("Dime tu calificacion del primer parcial:"))
parcial2=float(input("Dime tu calificacion del segundo parcial:"))
parcial3=float(input("Dime tu calificacion del tercer parcial:"))
final=float(input("Dime tu calificacion del examen final:"))
trabajo=float(input("Dime tu calificacion del trabajo final:"))

calificacion=(((parcial1+parcial2+parcial3)/3)*0.55+(final*0.3)+(trabajo*0.15))
             
print ("La calificación final es:  ", calificacion)




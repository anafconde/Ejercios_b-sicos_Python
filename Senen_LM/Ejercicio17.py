#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
#El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.
#version 1.0
#author Senén Lara

horas=int(input("Introduce la hora de partida: "))
minutos=int(input("Introduce el minuto de partida: "))
segundos=int(input("Introduce los segundos de partida: "))

horasseg=horas*3600
minutosseg=minutos*60

tiempoASeg=horasseg+minutosseg+segundos

tiempoB=int(input("Introduce el tiempo que has tardado en segundos hasta B: "))

tiempotardado=tiempoB+tiempoASeg

segundostard=tiempotardado%60
minutos1=tiempotardado/60
minutostard=minutos1%60
horastard=minutos1//60

print("Has llegado a las: ", horastard, "horas, ", minutostard , "minutos, ", segundostard , "segundos.")


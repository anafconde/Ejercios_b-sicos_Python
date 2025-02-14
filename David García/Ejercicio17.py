#Ejercicio 17
#Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

HH = int(input("Introduce la hora de salida (HH): "))
MM = int(input("Introduce los minutos de salida (MM): "))
SS = int(input("Introduce los segundos de salida (SS): "))
T = int(input("Introduce el tiempo de viaje (segundos): "))

segundos_salida = HH * 3600 + MM * 60 + SS
segundos_llegada = segundos_salida + T

HH_llegada = (segundos_llegada // 3600) % 24
MM_llegada = (segundos_llegada % 3600) // 60
SS_llegada = segundos_llegada % 60

horas_viaje = (segundos_llegada - segundos_salida) // 3600
minutos_viaje = ((segundos_llegada - segundos_salida) % 3600) // 60
segundos_viaje = (segundos_llegada - segundos_salida) % 60

print("La hora de llegada a la ciudad B es:", HH_llegada, ":", MM_llegada, ":", SS_llegada)
# Author: Luis Palacios
# Version: 1.0
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo que determine la hora de llegada a la ciudad B.

horas=int(input("Introduce la hora de salida: "))
minutos=int(input("Introduce el minuto de salida: "))
segundos=int(input("Introduce los segundos de salida: "))

hseg=horas*3600
mseg=minutos*60

tseg=hseg+mseg+segundos

tseg2=int(input("Introduce el tiempo que has tardado en segundos hasta B: "))

ttotal=tseg+tseg2

sllegada=ttotal%60
minahora=ttotal//60
mllegada=minahora%60
hllegada=minahora//60


print("Has llegado a las: ", hllegada, "horas, ", mllegada , "minutos, ", sllegada , "segundos.")
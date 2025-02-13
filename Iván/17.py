

# Author = Iván Suárez
# Version = 1.0
""" 
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la ciudad B.

"""
print("Introduce tu hora de salida")
hour = int(input("¿Cuántas horas?: "))
min = int(input("¿Cuántos minutos?: "))
sec = int(input("¿Cuántos segundos?: "))
time = int(input("¿Cuántos segundos has tardado en llegar?: "))

hour *= 3600
min *= 60
sec += hour+min
time += sec

tsec = time%60
t = time//60
tmin = t%60
thour = t//60

print (f"Has llegado a las {thour} h, {tmin} min, {tsec} seg")
#Lidia Castro Gutiérrez
#Versión 1

#18. Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

nombre=input("Dime tu nombre: ")
ape1=input("Dime tu primer apellido: ")
ape2=input("Dime tu segundo apellido: ")

iniciales = nombre[0].upper() + ape1[0].upper() + ape2[0].upper()

print(f"Las iniciales de tu nombre son {iniciales}")

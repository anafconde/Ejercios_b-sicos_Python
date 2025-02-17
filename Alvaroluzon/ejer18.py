# Alvaro Luzon Muñoz
#---version 1.0----
#Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.



nombre = input("Ingrese el nombre completo: ")


iniciales = "".join([parte[0].upper() for parte in nombre.split()])


print(f"Las iniciales son: {iniciales}")

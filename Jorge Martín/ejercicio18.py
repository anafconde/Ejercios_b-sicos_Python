#Autor
#Version
#Enunciado

nombre = input("Ingrese su nombre: ").strip()
apellido1 = input("Ingrese su primer apellido: ").strip()
apellido2 = input("Ingrese su segundo apellido: ").strip()

iniciales = nombre[0].upper() + apellido1[0].upper() + apellido2[0].upper()

print(f"Sus iniciales son: {iniciales}")

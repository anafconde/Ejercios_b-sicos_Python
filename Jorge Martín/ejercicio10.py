#Autor
#Version
#Enunciado

parcial1 = float(input("Ingrese la calificación del primer parcial: "))
parcial2 = float(input("Ingrese la calificación del segundo parcial: "))
parcial3 = float(input("Ingrese la calificación del tercer parcial: "))

examenfinal = float(input("Ingrese la calificación del examen final: "))

trabajofinal = float(input("Ingrese la calificación del trabajo final: "))

promedio_parciales = (parcial1 + parcial2 + parcial3) / 3

calificacionfinal = (promedio_parciales * 0.55) + (examenfinal * 0.30) + (trabajofinal * 0.15)

print(f"La calificación final es: {calificacionfinal:.2f}")

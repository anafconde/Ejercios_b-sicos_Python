# Autor: Mohamed Mchachi
# Versión: 1.0
# Enunciado:  Ejercicio 20: Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)


monedas_2e = float(input("¿Cuántas monedas de 2€ tienes? "))
monedas_1e = float(input("¿Cuántas monedas de 1€ tienes? "))
monedas_50c = float(input("¿Cuántas monedas de 50 céntimos tienes? "))
monedas_20c = float(input("¿Cuántas monedas de 20 céntimos tienes? "))
monedas_10c = float(input("¿Cuántas monedas de 10 céntimos tienes? "))


total_euros = (monedas_2e * 2) + (monedas_1e * 1) + (monedas_50c * 0.50) + (monedas_20c * 0.20) + (monedas_10c * 0.10)


print(f"Tienes un total de {total_euros:.2f} €")
#Ejercicio 20
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos)

monedas_2_euros = int(input("Introduce el número de monedas de 2 euros: "))
monedas_1_euro = int(input("Introduce el número de monedas de 1 euro: "))
monedas_50_centimos = int(input("Introduce el número de monedas de 50 céntimos: "))
monedas_20_centimos = int(input("Introduce el número de monedas de 20 céntimos: "))
monedas_10_centimos = int(input("Introduce el número de monedas de 10 céntimos: "))

total_centimos = (monedas_2_euros * 200) + (monedas_1_euro * 100) + (monedas_50_centimos * 50) + (monedas_20_centimos * 20) + (monedas_10_centimos * 10)

euros = total_centimos // 100
centimos = total_centimos % 100

print("Tienes", euros, "euros y", centimos, "céntimos")
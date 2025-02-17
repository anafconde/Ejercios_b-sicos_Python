# Alvaro Luzon Muñoz
#---version 1.0----
#Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).



d2 = int(input("Monedas de 2 euros: "))
d1 = int(input("Monedas de 1 euro: "))
d50 = int(input("Monedas de 50 céntimos: "))
d20 = int(input("Monedas de 20 céntimos: "))
d10 = int(input("Monedas de 10 céntimos: "))

total = (d2 * 2) + (d1 * 1) + (d50 * 0.50) + (d20 * 0.20) + (d10 * 0.10)

euros = int(total)
centimos = round((total - euros) * 100)

print(f"Total: {euros} euros y {centimos} céntimos.")

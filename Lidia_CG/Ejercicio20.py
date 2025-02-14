#Lidia Castro Gutiérrez
#Versión 1

#20. Diseñar un algoritmo que nos diga el dinero que tenemos (en euros y céntimos) después de pedirnos cuantas monedas tenemos (de 2€, 1€, 50 céntimos, 20 céntimos o 10 céntimos).

moneda2=float(input("Dime cuántas monedas de 2€ tienes: "))
moneda1=float(input("Dime cuántas monedas de 1€ tienes: "))
moneda50=float(input("Dime cuántas monedas de 50 céntimos tienes: "))
moneda20=float(input("Dime cuántas monedas de 20 céntimos tienes: "))
moneda10=float(input("Dime cuántas monedas de 10 céntimos tienes: "))

total=(moneda2*2)+(moneda1*1)+(moneda50*0.50)+(moneda20*0.20)+(moneda10*0.10)

print(f"Tienes {total}€")
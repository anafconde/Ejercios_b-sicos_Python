#Autor
#Version
#Enunciado

monedas_2e = int(input("Ingrese la cantidad de monedas de 2€: "))
monedas_1e = int(input("Ingrese la cantidad de monedas de 1€: "))
monedas_50c = int(input("Ingrese la cantidad de monedas de 50 céntimos: "))
monedas_20c = int(input("Ingrese la cantidad de monedas de 20 céntimos: "))
monedas_10c = int(input("Ingrese la cantidad de monedas de 10 céntimos: "))

total_euros = (monedas_2e * 2) + (monedas_1e * 1) + (monedas_50c * 0.50) + (monedas_20c * 0.20) + (monedas_10c * 0.10)

euros = int(total_euros)
centimos = int(round((total_euros - euros) * 100))

print(f"El total de dinero es: {euros} euros y {centimos} céntimos.")

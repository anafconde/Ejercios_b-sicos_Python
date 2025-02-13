

# Author = Iván Suárez
# Version = 1.0
# Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

prize = float(input("Introduce el precio para el descuento: "))
desc = prize*15/100
prize -=desc

print(f"El precio final es: {prize}")




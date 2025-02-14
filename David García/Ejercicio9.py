#Ejercicio 9
#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.

precio_original = float(input("Ingresa el precio original de la compra: "))
descuento = precio_original * 0.15
precio_final = precio_original - descuento
print(f"El precio final de la compra es: {precio_final}")
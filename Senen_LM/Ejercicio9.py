#Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
#version 1.0
#author Senén Lara

precio=float(input("Introduce el precio de tu producto: "))
desc=(precio*15)/100
precdesc=precio-desc
print("Deberás pagar: ", precdesc)

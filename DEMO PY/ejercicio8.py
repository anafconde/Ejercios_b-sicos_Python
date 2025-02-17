#Autor
#Version
#Enunciado

sueldo = float(input("Ingresa el sueldo base: "))

venta1 = float(input("Ingrese la primera venta: "))
venta2 = float(input("Ingrese la segunda venta: "))
venta3 = float(input("Ingrese la tercera venta: "))

comision = (venta1 + venta2 + venta3) * 0.10

total = sueldo + comision

print(f"Comisión total por ventas: {comision}")
print(f"Total a recibir en el mes: {total}")

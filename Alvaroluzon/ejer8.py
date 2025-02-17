# Alvaro Luzon Muñoz
#---version 1.0----
#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.



sueldo = float(input("Ingrese el sueldo base: "))


venta1 = float(input("Ingrese  la primera venta: "))
venta2 = float(input("Ingrese  la segunda venta: "))
venta3 = float(input("Ingrese  la tercera venta: "))


comision = (venta1 + venta2 + venta3) * 0.10


sueldototal = sueldo + comision

print("Resultados:")
print("Comisión total por ventas: $",comision)
print("Sueldo total del mes: $", sueldototal)
